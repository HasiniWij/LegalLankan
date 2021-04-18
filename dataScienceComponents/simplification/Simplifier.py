import spacy
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import torch
from transformers import BertTokenizer, BertForMaskedLM
from wordfreq import zipf_frequency
from pycorenlp import *

nlp = StanfordCoreNLP("https://corenlp.run/")


class Simplifier:
    is_first_run = True
    bert_model = 'bert-large-uncased'
    model = ""

    def __init__(self):
        # bert_model = 'bert-large-uncased'
        if Simplifier.is_first_run:
            Simplifier.model = BertForMaskedLM.from_pretrained(Simplifier.bert_model)
            Simplifier.is_first_run = False
        self.tokenizer = BertTokenizer.from_pretrained(Simplifier.bert_model)
        Simplifier.model.eval()
        self.conjunction_list = ["for", "and"]

    def remove_punctuation(self, input_text):
        x = re.sub("[^-9A-Za-z ]", "", input_text)
        return x

    # the word is turned to lower case and characters other than letters are removed
    def cleaned_word(self, word):
        word = re.sub('[^a-zA-Z]', ' ', word)
        return word.lower().strip()

    def tokenized(self, sentence):
        nltk_tokens = nltk.word_tokenize(sentence)
        return nltk_tokens

    def sentences_list(self, token_list1, token_list2):
        str1 = " "
        str2 = " "
        broken_list = [str1.join(token_list1), str2.join(token_list2)]
        return broken_list

    #     basic Named Entity Recognition code
    def NER_identifier(self, text):
        entity_list = []
        # nlp_ner = en_core_web_sm.load()
        nlp_ner = spacy.load("en_core_web_sm")
        doc = nlp_ner(text)
        for x in doc.ents:
            entity_tokens = self.tokenizer.tokenize(x.text)
            for word in entity_tokens:
                entity_list.append(word)
        return entity_list

    # BERT model to predict candidates for identified complex words
    def get_bert_candidates(self, input_text, word):

        numb_predictions_displayed = 2
        list_candidates_bert = []
        names_enitites = self.NER_identifier(input_text)
        lowercase_word = word.lower()

        if lowercase_word not in names_enitites:
            replace_word_mask = input_text.replace(word, '[MASK]')
            text = f'[CLS]{replace_word_mask} [SEP] {input_text} [SEP] '
            tokenized_text = self.tokenizer.tokenize(text)

            index_count = 0
            mask_index = 0
            for token in tokenized_text:
                if token == "[MASK]":
                    mask_index = index_count
                    break
                index_count += 1

            indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)
            segments_ids = [0] * len(tokenized_text)
            tokens_tensor = torch.tensor([indexed_tokens])
            segments_tensors = torch.tensor([segments_ids])

            # Predict all tokens
            with torch.no_grad():
                outputs = Simplifier.model(tokens_tensor, token_type_ids=segments_tensors)
                predictions = outputs[0][0][mask_index]
            predicted_ids = torch.argsort(predictions, descending=True)[:numb_predictions_displayed]
            predicted_tokens = self.tokenizer.convert_ids_to_tokens(list(predicted_ids))
            list_candidates_bert.append((word, predicted_tokens))

        return list_candidates_bert

    def get_lexically_simplified_text(self, piece_list):

        lexically_simplified_pieces = []
        ps = LancasterStemmer()
        for sentence in piece_list:
            input_no_punctuation = self.remove_punctuation(sentence)
            list_of_words = word_tokenize(input_no_punctuation)

            for word in list_of_words:
                word = self.cleaned_word(word)
                if zipf_frequency(word, 'en') < 4:
                    candidates = self.get_bert_candidates(input_no_punctuation, word)
                    for candidate in candidates:
                        if candidate[0] == word:

                            if zipf_frequency(candidate[1][0], 'en') > zipf_frequency(candidate[1][1], 'en'):
                                replacement = candidate[1][0]
                            else:
                                replacement = candidate[1][1]
                            if ps.stem(replacement) == ps.stem(word) or (not replacement.isalpha()):
                                replacement = word
                            sentence = sentence.replace(word, replacement)

            lexically_simplified_pieces.append(sentence)
        return lexically_simplified_pieces

    # checking whether a sentence is complete using a parse tree
    # checking whether a sentence has a conjunction
    def word_is_a_conjunction(self, word):
        for conjunction in self.conjunction_list:
            if word == conjunction:
                return True
        return False

    def get_syntactically_simplified_text(self, input_list):

        for i in range(0, len(input_list), 2):

            # input_piece is a string
            broken_sentences = input_list[i], input_list[i + 1]
            input_piece = input_list[i + 1]

            # if the 2 sentences broken from the conjunction form complete sentences, the splitting is successful
            text = re.sub(r"([.,?()\[\]])", "", input_piece)
            count = 0

            if (len(text.split()) > 25) and any(conjunction in text for conjunction in self.conjunction_list):

                for word in self.tokenized(text):
                    if self.word_is_a_conjunction(word):
                        token_list = self.tokenized(text)
                        sentences = self.sentences_list(token_list[:count], token_list[count + 1:])

                        if self.confirm_syntactic_simplification(
                                sentences[0]) and self.confirm_syntactic_simplification(sentences[1]):
                            broken_sentences = [input_list[i], sentences[0], sentences[1]]
                            break
                    count += 1

        return broken_sentences

    def confirm_syntactic_simplification(self, text):
        sub_sub_trees = []
        parser = nlp.annotate(text, properties={"annotators": "parse", "outputFormat": "json"})
        try:
            sent_tree = nltk.tree.ParentedTree.fromstring(parser["sentences"][0]["parse"])
            sub_trees = list(sent_tree.subtrees())

            if sub_trees[1].label() == "S":
                for sub_sub_tree in sub_trees[1]:
                    sub_sub_trees.append(sub_sub_tree.label())

                if ("VP" and "NP") in sub_sub_trees:
                    return True
        except:
            return False

        return False

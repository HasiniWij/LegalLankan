import en_core_web_sm
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import torch
from transformers import BertTokenizer, BertForMaskedLM
from wordfreq import zipf_frequency
from pycorenlp import *

nlp = StanfordCoreNLP("https://corenlp.run/")


# the word is turned to lower case and characters other than letters are removed
def cleaned_word(word):
    # Remove links
    # word = re.sub(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])
    # *', '', word, flags=re.MULTILINE)
    # word = re.sub('[\W]', ' ', word)
    word = re.sub('[^a-zA-Z]', ' ', word)
    return word.lower().strip()


# Complex Word Identification
def get_list_cwi_predictions(input_text):
    list_cwi_predictions = []
    list_of_words = word_tokenize(input_text)
    for word in list_of_words:
        word = cleaned_word(word)
        if zipf_frequency(word, 'en') < 4:
            list_cwi_predictions.append(True)
        else:
            list_cwi_predictions.append(False)
    return list_cwi_predictions


def remove_punctuation(input_text):
    x = re.sub("[^-9A-Za-z ]", "", input_text)
    return x


def confirm_syntactic_simplification(text):
    sub_sub_trees = []
    parser = nlp.annotate(text, properties={"annotators": "parse", "outputFormat": "json"})
    sent_tree = nltk.tree.ParentedTree.fromstring(parser["sentences"][0]["parse"])
    sent_tree.pretty_print()
    sub_trees = list(sent_tree.subtrees())

    if sub_trees[1].label() == "S":
        for sub_sub_tree in sub_trees[1]:
            sub_sub_trees.append(sub_sub_tree.label())

        if ("VP" and "NP") in sub_sub_trees:
            return True
    return False


def tokenized(sentence):
    nltk_tokens = nltk.word_tokenize(sentence)
    return nltk_tokens


def sentences_list(token_list1, token_list2):
    str1 = " "
    str2 = " "
    broken_list = [str1.join(token_list1), str2.join(token_list2)]
    return broken_list


class Simplifier:

    def __init__(self):

        bert_model = 'bert-large-uncased'
        self.tokenizer = BertTokenizer.from_pretrained(bert_model)
        self.model = BertForMaskedLM.from_pretrained(bert_model)
        self.model.eval()
        self.conjunction_list = ["for", "and"]

    # basic Named Entity Recognition code
    def NER_identifier(self, text):
        entity_list = []
        nlp_ner = en_core_web_sm.load()
        doc = nlp_ner(text)
        for x in doc.ents:
            entity_tokens = self.tokenizer.tokenize(x.text)
            for word in entity_tokens:
                entity_list.append(word)
        return entity_list

    # BERT model to predict candidates for identified complex words
    def get_bert_candidates(self, input_text, list_cwi_predictions, numb_predictions_displayed=2):

        list_candidates_bert = []
        names_enitites = self.NER_identifier(input_text)
        for word, pred in zip(input_text.split(), list_cwi_predictions):

            lowercase_word = word.lower()

            if pred and lowercase_word not in names_enitites:
                replace_word_mask = input_text.replace(word, '[MASK]')
                text = f'[CLS]{replace_word_mask} [SEP] {input_text} [SEP] '
                tokenized_text = self.tokenizer.tokenize(text)
                masked_index = [i for i, x in enumerate(tokenized_text) if x == '[MASK]'][0]
                indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)
                segments_ids = [0] * len(tokenized_text)
                tokens_tensor = torch.tensor([indexed_tokens])
                segments_tensors = torch.tensor([segments_ids])

                # Predict all tokens
                with torch.no_grad():
                    outputs = self.model(tokens_tensor, token_type_ids=segments_tensors)
                    predictions = outputs[0][0][masked_index]
                predicted_ids = torch.argsort(predictions, descending=True)[:numb_predictions_displayed]
                predicted_tokens = self.tokenizer.convert_ids_to_tokens(list(predicted_ids))
                list_candidates_bert.append((word, predicted_tokens))

        return list_candidates_bert

    def get_lexically_simplified_text(self, input_piece):

        input_no_punctuation = remove_punctuation(input_piece)
        prediction_list = get_list_cwi_predictions(input_no_punctuation)

        ps = LancasterStemmer()

        candidates = self.get_bert_candidates(input_no_punctuation, prediction_list)

        for word, prediction in zip(input_no_punctuation.split(), prediction_list):
            if prediction:
                for candidate in candidates:
                    if candidate[0] == word:
                        replacement = ""
                        if zipf_frequency(candidate[1][0], 'en') > zipf_frequency(candidate[1][1], 'en'):
                            replacement = candidate[1][0]
                        else:
                            replacement = candidate[1][1]
                        if ps.stem(replacement) == ps.stem(word) or (not replacement.isalpha()):
                            replacement = word
                        input_piece = input_piece.replace(word, replacement)

        return input_piece

    # checking whether a sentence is complete using a parse tree
    # checking whether a sentence has a conjunction
    def word_is_a_conjunction(self, word):
        for conjunction in self.conjunction_list:
            if word == conjunction:
                return True
        return False

    def get_syntactically_simplified_text(self, input_piece):
        # if the 2 sentences broken from the conjunction form complete sentences, the splitting is successful
        text = re.sub(r"([.,?()\[\]])", "", input_piece)
        count = 0
        broken_sentences = []
        if (len(text.split()) > 25) and any(conjunction in text for conjunction in self.conjunction_list):

            for word in tokenized(text):
                if self.word_is_a_conjunction(word):
                    token_list = tokenized(text)
                    sentences = sentences_list(token_list[:count], token_list[count + 1:])
                    print("sentences", sentences)
                    if confirm_syntactic_simplification(sentences[0]) and \
                            confirm_syntactic_simplification(sentences[1]):
                        broken_sentences = [sentences[0], sentences[1]]
                        break
                count += 1

        return broken_sentences

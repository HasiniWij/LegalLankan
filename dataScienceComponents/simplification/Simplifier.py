import spacy     # for NER
import nltk      # for text preprocessing tasks
import re        # to find or replace characters
import torch     # enables the BERT model to predict candidates
from transformers import BertTokenizer, BertForMaskedLM  # to load pre-trained model needed for complex word replacements
from wordfreq import zipf_frequency    # to get the complexity (zipf frequency) level of a word
from nltk.tokenize import sent_tokenize



class Simplifier:

    is_first_run = True
    bert_model = 'bert-base-uncased'
    model = ""

    def __init__(self):
        # bert_model = 'bert-large-uncased'    # the preferred model but causes timeouts after deployment
        if Simplifier.is_first_run:
            Simplifier.model = BertForMaskedLM.from_pretrained(Simplifier.bert_model)  # loads BERT model
            Simplifier.is_first_run = False
        self.tokenizer = BertTokenizer.from_pretrained(Simplifier.bert_model)
        Simplifier.model.eval()
        # self.conjunction_list = ["for", "and"]



    def NER_identifier(text):

        entity_list = []
        sentence_list = sent_tokenize(text)
        nlp = spacy.load('en_core_web_sm')

        for sentence in sentence_list:
            nlp_sentence = nlp(sentence)
            if nlp_sentence.ents:
                for ent in nlp_sentence.ents:
                    if ent.text not in entity_list:
                        entity_list.append(ent.text)

        return (entity_list)

    def identify_complex_words(self,content, zip_value=4):
        cwi_words = []

        content = content.replace("\n", "")
        words = content.split()


        enitites = Simplifier.NER_identifier(content)

        all_entities=""
        for sentence in enitites:
            all_entities=all_entities+ " "+ sentence

        names_enitites=all_entities.split()


      
        for word in words:
            cleaned_word = word.lower().strip()
            if zipf_frequency(cleaned_word,'en') < zip_value and word.isalpha() and \
                    word not in names_enitites and word not in cwi_words:
                cwi_words.append(word)
        return cwi_words



    def get_bert_candidates(self,input_text, word):
        word.lower().strip()
        input_text = re.sub("[^-9A-Za-z ]", "", input_text)
        numb_predictions_displayed = 4

        replace_word_mask = input_text.replace(word, '[MASK]')  # complex word is masked
        text = f'[CLS]{replace_word_mask} [SEP] {input_text} [SEP] '
        tokenized_text = self.tokenizer.tokenize(text)  # tokenizing the masked text
        mask_index = [i for i, x in enumerate(tokenized_text) if x == '[MASK]'][0]
        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)  # creating ids for tokens
        segments_ids = [0] * len(tokenized_text)  # list zeros of length being number of tokens
        tokens_tensor = torch.tensor([indexed_tokens])  # creating a matrix of token ids
        segments_tensors = torch.tensor([segments_ids])

        with torch.no_grad():  # to reduce memory consumption
            outputs = Simplifier.model(tokens_tensor, token_type_ids=segments_tensors)  # using BERT model to find candidates
            predictions = outputs[0][0][mask_index]
            predicted_ids = torch.argsort(predictions, descending=True)[
                            :numb_predictions_displayed]  # sorting candidates according to relevancy
            predicted_tokens = self.tokenizer.convert_ids_to_tokens(list(predicted_ids))
            return predicted_tokens  # complex word candidates are returned



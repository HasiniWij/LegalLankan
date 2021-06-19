import jieba  # used to fot text segmentation
import pickle  # models are stored as pickles and loaded to this file

from gensim import corpora, models, similarities
from nltk import WordNetLemmatizer, sent_tokenize
from nltk.corpus import stopwords
import numpy as np


class Extractor:

    def __init__(self):

        common_path = "dataScienceComponents/extraction/models/"

        # loading the similarity matrix which stores document similarity data of all documents within the category
        matrix_path = common_path + "matrix.pickle"
        with open(matrix_path, 'rb') as matrix:
            self.matrix = pickle.load(matrix)

        # loading the dictionary of the category
        dictionary_path = common_path + "dic.pickle"
        with open(dictionary_path, 'rb') as cat_dictionary:
            self.dictionary = pickle.load(cat_dictionary)

        # loading the tfidf model of the category
        tfidf_path = common_path + "tfdif.pickle"
        with open(tfidf_path, 'rb') as tfidf_model:
            self.tfidf = pickle.load(tfidf_model)

        with open("data.pickle", 'rb') as data:
            self.data = pickle.load(data)

    def get_query_keywords(self, query):
        query_lowered = query.lower()  # all letters are turned into lowercase

        punctuation_signs = list("?:!.,;")  # punctuation signs are removed
        for punctuation_sign in punctuation_signs:
            query_lowered = query_lowered.replace(punctuation_sign, '')

        query_lowered = query_lowered.replace("'s", "")  # apostrophes are removed

        wordnet_lemmatizer = WordNetLemmatizer()  # all query words are lemmatized
        lemmatized_query_words_list = []

        query_words = query_lowered.split(" ")
        for word in query_words:
            lemmatized_query_words_list.append(wordnet_lemmatizer.lemmatize(word, pos="v"))

        stop_words = list(stopwords.words('english'))  # all stop words within the query are removed
        for word in lemmatized_query_words_list:
            if word in stop_words:
                lemmatized_query_words_list.remove(word)

        # all keywords after preprocessing, turned into a string of words, and returned
        cleaned_query = ' '.join(map(str, lemmatized_query_words_list))

        return cleaned_query

    def create_matrix_tfidf_dic(self, data):
        # dictionary - convert search word to vector
        # jieba - cuts the kewords into segments
        data = [jieba.lcut(text) for text in data]
        dictionary = corpora.Dictionary(data)
        # counts the word features of the dictionary of texts
        feature_cnt = len(dictionary.token2id)
        # counts the number of occurrences of a word within the corpus
        corpus = [dictionary.doc2bow(text) for text in data]
        # Creates a tf-idf model
        tfidf = models.TfidfModel(corpus)
        # Convert and index the corpus to check for similarity
        matrix = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)
        return tfidf,dictionary,matrix

    def get_ranked_documents(self, keywords):


        documents_with_a_rank = {}

        # dictionary - convert search word to vector
        # jieba - cuts the keywords into segments
        # doc2bow - counts the number of occurrences of a word within the corpus
        kw_vector = self.dictionary.doc2bow(jieba.lcut(keywords))

        sim = self.matrix[self.tfidf[kw_vector]]  # checks the similarity of each document within the category

        for i in range(len(sim)):
            if sim[i] > 0.00:
                documents_with_a_rank[i] = sim[i]

        five_ranked_documents = sorted(documents_with_a_rank, key=documents_with_a_rank.get, reverse=True)[:7]

        relevant_docs= []
        for doc in five_ranked_documents:
            title = self.data['title'][doc]
            sentence_list = sent_tokenize(self.data['content'][doc])

            segmented_doc = []
            for i in range(0, len(sentence_list), 4):
                content = ""
                if i + 4 < len(sentence_list):
                    content = sentence_list[i] + sentence_list[i + 1] + sentence_list[i + 2] + sentence_list[i + 3]
                    segmented_doc.append(content)

            tfidf_segment, dictionary_segment, matrix_segment=self.create_matrix_tfidf_dic(segmented_doc)


            # segmented_doc_process = [jieba.lcut(text) for text in segmented_doc]
            # dictionary_segment = corpora.Dictionary(segmented_doc_process)
            # # counts the word features of the dictionary of texts
            # feature_cnt = len(dictionary_segment.token2id)
            # # counts the number of occurrences of a word within the corpus
            # corpus = [dictionary_segment.doc2bow(text) for text in segmented_doc_process]
            # # Creates a tf-idf model
            # tfidf_segment = models.TfidfModel(corpus)
            # Convert and index the corpus to check for similarity
            # matrix_segment = similarities.SparseMatrixSimilarity(tfidf_segment[corpus], num_features=feature_cnt)

            kw_vector_segment = dictionary_segment.doc2bow(jieba.lcut(keywords))
            # checks the similarity of each document within the category
            sim_segment = matrix_segment[tfidf_segment[kw_vector_segment]]
            print("sim_segment: ", sim_segment)

            index = np.where(sim_segment == np.amax(sim_segment))
            print("index: ", index[0][0])

            content_segment = segmented_doc[index[0][0]]+"..."
            title_segment={'title':title,'content':content_segment}
            relevant_docs.append(title_segment)


            # title_segment[title] = content_segment + "..."

        return relevant_docs

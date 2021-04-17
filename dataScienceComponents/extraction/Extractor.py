import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models, similarities
import jieba
import pickle
import pandas as pd


class Extractor:

    def __init__(self, category):

        common_path = "./dataScienceComponents/extraction/models/" + category + "/" + category

        # loading the similarity matrix which stores document similarity data of all documents within the category
        matrix_path = common_path + "_matrix.pickle"

        with open(matrix_path, 'rb') as matrix:
            self.category_matrix = pickle.load(matrix)

        # loading the dictionary of the category
        dictionary_path = common_path + "_dic.pickle"
        with open(dictionary_path, 'rb') as cat_dictionary:
            self.dictionary = pickle.load(cat_dictionary)

        # loading the tfidf model of the category
        tfidf_path = common_path + "_tfdif.pickle"
        with open(tfidf_path, 'rb') as tfidf_model:
            self.tfidf = pickle.load(tfidf_model)

        # loading the piece index mapping with matrix index of the category
        df_path = common_path + "-df.pickle"
        with open(df_path, 'rb') as mapping:
            self.df = pickle.load(mapping)

    def get_ranked_documents(self, keywords):
        documents_with_a_rank = {}

        # dictionary - convert search word to vector
        # jieba - cuts the keywords into segments
        # doc2bow - counts the number of occurrences of a word within the corpus
        kw_vector = self.dictionary.doc2bow(jieba.lcut(keywords))

        sim = self.category_matrix[self.tfidf[kw_vector]]  # checks the similarity of each document within the category

        for i in range(len(sim)):
            if sim[i] > 0.00:
                documents_with_a_rank[i] = sim[i]

        five_ranked_documents = sorted(documents_with_a_rank, key=documents_with_a_rank.get, reverse=True)[:5]
        five_ranked_piece_index = []
        for doc in five_ranked_documents:
            for index, row in self.df.iterrows():
                if doc == index:
                    five_ranked_piece_index.append(row['pieceIndex'])
                    break

        return five_ranked_piece_index

    def create_matix_dic_tfidf(self, category_df, category):
        # doucmnets should be ranked according legName, pieceName,content
        data = []
        for index, row in category_df.iterrows():
            full_content = row['legName'] + " " + row['pieceName'] + " " + row['content']
            data.append(full_content)

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
        common_path = "dataScienceComponents/extraction/models/" + category + "/" + category

        with open(common_path + '_matrix.pickle', 'wb') as output:
            pickle.dump(matrix, output)

        with open(common_path + '_dic.pickle', 'wb') as output:
            pickle.dump(dictionary, output)

        with open(common_path + '_tfdif.pickle', 'wb') as output:
            pickle.dump(tfidf, output)







import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models, similarities
import jieba
import pickle
import pandas as pd

class Extractor:

    def __init__(self,category):
        common_path="../dataScienceComponents/extraction/models/"+category+"/"+category
        # loading the similarity matrix which stores document similarity data of all documents within the category
        matrix_path = common_path+"_matrix.pickle"
        # matrix_path = "/Users/Shontaal/Documents/GitHub/SDGP/backend/extraction/models/rights/rights_matrix.pickle"
        with open(matrix_path, 'rb') as matrix:
            self.category_matrix = pickle.load(matrix)

        # loading the dictionary of the category
        # dictionary_path = "/Users/Shontaal/Documents/GitHub/SDGP/backend/extraction/models/rights/rights_dic.pickle"
        dictionary_path =common_path+"_dic.pickle"
        with open(dictionary_path, 'rb') as cat_dictionary:
            self.dictionary = pickle.load(cat_dictionary)

        # loading the tfidf model of the category
        tfidf_path =common_path+"_tfdif.pickle"
        # tfidf_path = "/Users/Shontaal/Documents/GitHub/SDGP/backend/extraction/models/rights/rights_tfdif.pickle"
        with open(tfidf_path, 'rb') as tfidf_model:
            self.tfidf = pickle.load(tfidf_model)

        # loading the piece index mapping with matrix index of the category
        piece_index_mapping_path = common_path+"-pieceIndex-mapping.pickle"
            # "/Users/Shontaal/Documents/GitHub/SDGP/backend/extraction/models/rights/rights-pieceIndex-mapping.pickle"
        with open(piece_index_mapping_path, 'rb') as mapping:
            self.piece_index_mapping = pickle.load(mapping)

    def get_ranked_documents(self,keywords):
        documnets_with_a_rank= {}

        # dictionary - convert search word to vector
        # jieba - cuts the keywords into segments
        # doc2bow - counts the number of occurrences of a word within the corpus
        kw_vector = self.dictionary.doc2bow(jieba.lcut(keywords))

        sim = self.category_matrix[self.tfidf[kw_vector]]  # checks the similarity of each document within the category

        for i in range(len(sim)):
            if sim[i] > 0.00:
                documnets_with_a_rank[i]=sim[i]

        five_ranked_documents = sorted(documnets_with_a_rank, key=documnets_with_a_rank   .get, reverse=True)[:5]
        five_ranked_piece_index=[]
        for doc in five_ranked_documents:
            for index, row in self.piece_index_mapping.iterrows():
                if doc==index:
                    five_ranked_piece_index.append(row['pieceIndex'])
                    break

        return five_ranked_piece_index









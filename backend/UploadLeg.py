import pickle
import pandas as pd

from backend.DocumentSplitter import DocumentSplitter  # used to split the document into pieces
from dataScienceComponents.classification.Classifier import Classifier  # used to classify the the document
from dataScienceComponents.extraction.Extractor import Extractor


class UploadLeg:

    def upload_act(self, content,title):

        with open("data.pickle", 'rb') as data_df:
            data_df = pickle.load(data_df)

        with open("title_category.pickle", 'rb') as data:
            title_cat = pickle.load(data)


        C = Classifier("dataScienceComponents/classification/models/svm.pickle", "dataScienceComponents"
                                                                    "/classification/models/tfidf.pickle")
        category = C.get_category_of_text(title + content)



        df=pd.DataFrame({"title": [title],"category": [category]})
        title_cat.append(df)

        df2 = pd.DataFrame({"title": [title], "content": [content]})
        data_df.append(df2)


        data = []
        for index, row in data_df.iterrows():
            data.append(row['title'] + " " + row['content'])

        E=Extractor()
        tfidf,dictionary,matrix=E.create_matrix_tfidf_dic(data)

        with open('dataScienceComponents/extraction/models/matrix.pickle', 'wb') as output:
            pickle.dump(matrix, output)

        with open('dataScienceComponents/extraction/models/dic.pickle', 'wb') as output:
            pickle.dump(dictionary, output)

        with open('dataScienceComponents/extraction/models//tfdif.pickle', 'wb') as output:
            pickle.dump(tfidf, output)



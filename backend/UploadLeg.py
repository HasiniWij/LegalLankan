import pickle

from backend.DocumentSplitter import DocumentSplitter  # used to split the document into pieces
from dataScienceComponents.classification.Classifier import Classifier  # used to classify the the document
from dataScienceComponents.extraction.Extractor import Extractor


class UploadLeg:
    def __init__(self):
        with open("data.pickle", 'rb') as data_df:
            self.data_df = pickle.load(data_df)

        with open("title_category.pickle", 'rb') as data:
            self.title_cat = pickle.load(data)


    def upload_act(self, content,title):
        self.update_data(title, content)
        self.save_pickles()



    def upload_core_leg(self, full_core_leg):

        d = DocumentSplitter()
        leg_name, split_core_leg = d.split_core_legislation(full_core_leg)

        u = UploadLeg()

        for item in split_core_leg:
            title = leg_name + " - " + item["chapterTitle"]
            content = item["chapterContent"]
            u.upload_act(content, title)

    def update_data(self,title,content):
        C = Classifier("dataScienceComponents/classification/models/svm.pickle", "dataScienceComponents"
                                                                                 "/classification/models/tfidf.pickle")
        category = C.get_category_of_text(title + content)
        print("cat", category)

        new_row = {'title': title, 'category': category}
        self.title_cat = self.title_cat.append(new_row, ignore_index=True)

        new_row_2 = {'title': title, 'content': content}
        self.data_df = self.data_df.append(new_row_2, ignore_index=True)

        print("data: ", self.data_df)
        print("title: ", self.title_cat)


    def save_pickles(self):

        data = []
        for index, row in self.data_df.iterrows():
            data.append(row['title'] + " " + row['content'])

        E = Extractor()
        tfidf, dictionary, matrix = E.create_matrix_tfidf_dic(data)

        with open('dataScienceComponents/extraction/models/matrix.pickle', 'wb') as output:
            pickle.dump(matrix, output)

        with open('dataScienceComponents/extraction/models/dic.pickle', 'wb') as output:
            pickle.dump(dictionary, output)

        with open('dataScienceComponents/extraction/models//tfdif.pickle', 'wb') as output:
            pickle.dump(tfidf, output)

        with open('data.pickle', 'wb') as output:
            pickle.dump(self.data_df, output)

        with open('title_category.pickle', 'wb') as output:
            pickle.dump(self.title_cat, output)




import pickle

from backend.DocumentSplitter import DocumentSplitter  # used to split the document into pieces
from dataScienceComponents.classification.Classifier import Classifier  # used to classify the the document
from dataScienceComponents.extraction.Extractor import Extractor


class UploadLeg:

    def upload_act(self, content,title):

        with open("data.pickle", 'rb') as data_df:
            data_df = pickle.load(data_df)

        with open("title_category.pickle", 'rb') as data:
            title_cat = pickle.load(data)

        data_df,title_cat=self.cat(title, content, title_cat, data_df)

        data = []
        for index, row in data_df.iterrows():
            data.append(row['title'] + " " + row['content'])

        E=Extractor()
        tfidf,dictionary,matrix=E.create_matrix_tfidf_dic(data)

        self.save_pickles(matrix,dictionary,tfidf,data_df,title_cat)



    def upload_core_leg(self, full_core_leg):

        d = DocumentSplitter()
        leg_name, split_core_leg = d.split_core_legislation(full_core_leg)

        u = UploadLeg()

        for item in split_core_leg:
            title = leg_name + " - " + item["chapterTitle"]
            content = item["chapterContent"]
            u.upload_act(content, title)

    def cat(self,title,content,title_cat,data_df):
        C = Classifier("dataScienceComponents/classification/models/svm.pickle", "dataScienceComponents"
                                                                                 "/classification/models/tfidf.pickle")
        category = C.get_category_of_text(title + content)
        print("cat", category)

        new_row = {'title': title, 'category': category}
        title_cat = title_cat.append(new_row, ignore_index=True)

        new_row_2 = {'title': title, 'content': content}
        data_df = data_df.append(new_row_2, ignore_index=True)

        print("data: ", data_df)
        print("title: ", title_cat)
        return data_df,title_cat

    def save_pickles(self,matrix,dictionary,tfidf,data_df,title_cat):
        with open('dataScienceComponents/extraction/models/matrix.pickle', 'wb') as output:
            pickle.dump(matrix, output)

        with open('dataScienceComponents/extraction/models/dic.pickle', 'wb') as output:
            pickle.dump(dictionary, output)

        with open('dataScienceComponents/extraction/models//tfdif.pickle', 'wb') as output:
            pickle.dump(tfidf, output)

        with open('data.pickle', 'wb') as output:
            pickle.dump(data_df, output)

        with open('title_category.pickle', 'wb') as output:
            pickle.dump(title_cat, output)




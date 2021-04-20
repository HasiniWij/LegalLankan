import pickle
import pandas as pd
from backend.DatabaseConnection import DatabaseConnection
from backend.DocumentSplitter import DocumentSplitter
from dataScienceComponents.classification.Classifier import Classifier


class UploadLeg:

    def upload_data_of_piece(self, text):
        splitter = DocumentSplitter()
        legislation_name, list_dictionary_piece = splitter.split_core_legislation(text)
        legislation_name = legislation_name.strip()

        print("2-Doc split done")

        categories = []

        for piece_dictionary in list_dictionary_piece:
            content = piece_dictionary.get("content")
            title = piece_dictionary.get("pieceTitle")

            C = Classifier("dataScienceComponents/classification/models/svm.pickle", "dataScienceComponents"
                                                                                     "/classification/models/tfidf"
                                                                                     ".pickle")

            piece_category = C.get_category_of_text(title + content)
            categories.append(piece_category)

            count_dict = {i: categories.count(i) for i in categories}

            final_category = max(count_dict, key=count_dict.get)

        if final_category == "family":
            category_code = "FA"

        elif final_category == "crime":
            category_code = "CR"

        elif final_category == "rights":
            category_code = "RI"

        elif final_category == "employment":
            category_code = "EM"
        else:
            category_code = "OT"

        db = DatabaseConnection("classify-legislation")
        insert_leg_sql = "INSERT INTO legislation (legislationName, categoryIndex) VALUES (%s, %s)"
        val = (legislation_name, category_code)
        db.insertToDB(insert_leg_sql, val)
        print("3-Leg name inserted")

        sql = '''select l.legislationIndex from legislation l where legislationName = ''' + '"' + str(
            legislation_name) + '"'
        sql_result = db.selectFromDB(sql)
        leg_index = sql_result["legislationIndex"][0]
        print("3-Leg index selected ", leg_index)

        for piece_dictionary in list_dictionary_piece:
            content = piece_dictionary.get("content")
            title = piece_dictionary.get("pieceTitle")

            db = DatabaseConnection("classify-legislation")
            sql = "INSERT INTO piece ( pieceTitle,content,legislationIndex) VALUES (%s, %s,%s)"
            val = (title, content, leg_index)
            db.insertToDB(sql, val)

        print("4-content inserted")

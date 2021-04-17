import pickle
import pandas as pd
from backend.DatabaseConnection import DatabaseConnection
from dataScienceComponents.classification.Classifier import Classifier


class uploadLeg:
    def __init__(self,  title,content):
        self.title=title
        self.content=content

    def upload_data_of_piece(self,leg_index,legislation_name):
        C = Classifier()

        piece_category = C.get_category_of_text( self.title+ self.content)

        if piece_category=="family":
            category_code="FA"

        elif piece_category=="crime":
            category_code="CR"

        elif piece_category=="rights":
            category_code="RI"

        elif piece_category=="employment":
            category_code="EM"

        else:
            category_code = "OT"

        db = DatabaseConnection("classify-legislation")
        sql = "INSERT INTO pieceCategory ( pieceTitle,content,legislationIndex,categoryIndex) VALUES (%s, %s,%s,%s)"
        val = (self.title+ self.content,leg_index,category_code)
        db.insertToDB(sql, val)

        sql = "select pieceIndex from piece where pieceTitle=" + self.title +" AND content="+self.content
        sql_result = db.selectFromDB(sql)
        piece_index = sql_result["pieceIndex"][0]

        df_path = "dataScienceComponents/extraction/models/" + piece_category + "/" + piece_category+"-df"
        with open(df_path, 'rb') as df:
            df_cat = pickle.load(df)
        new_df = pd.DataFrame({"pieceIndex":[piece_index],"legislationName":[legislation_name],"pieceTitle":[self.title],"content":[self.content]})
        df_cat.append(new_df)
        df.close()

        with open(df_path, 'wb') as df:
            pickle.dump(df_cat, df)
        df.close()
        other_path = "dataScienceComponents/extraction/models/other/other-df"
        with open(other_path, 'rb') as df_other:
            other = pickle.load(df_other)
        other.append(new_df)
        df_other.close()

        with open(df_path, 'wb') as df_other:
            pickle.dump(df_cat, df_other)
        df_other.close()
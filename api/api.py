# from flask import Flask, request
# from classification.Classifier import Classifier
# # from .Classifier import get_query_keywords
# from extraction.Extractor import Extractor
#
# app = Flask(__name__)
#
# # @app.route('/', methods=['GET'])
# # def index():
# #     return{
# #         'name':'Hello world'
# #     }
#
# @app.route('/search', methods = ['GET', 'POST'])
# def result():
#     if request.method == 'GET':
#         query = request.args.get('query', None)
#         if query:
#             C = Classifier("/Users/Shontaal/Documents/GitHub/SDGP/api/classification/models/best_rfc.pickle", "/Users/Shontaal/Documents/GitHub/SDGP/api/classification/models/tfidf.pickle")
#             queryCategory = C.get_category_of_text(query)
#
#             E = Extractor(queryCategory)
#             extracted = E.get_ranked_documents("main human rights")
#
#             listToStr = ' '.join(map(str, extracted))
#             print("Query: " + query + '\n' + "Query Category: " + queryCategory + '\n' + "Extraction Piece Index: " + listToStr)
#             return "Query: " + query + " ||| " + "Query Category: " + queryCategory + " ||| " + "Extraction Piece Index: " + listToStr
#
#         return "No place information is given"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


import pandas as pd
import pymysql
import json
from flask import Flask
from json import JSONEncoder
from dataScienceComponents.classification.Classifier import Classifier
from dataScienceComponents.extraction.Extractor import Extractor

app = Flask(__name__)


class QueryAnswer():
    def __init__(self, sql_result):
        p_title= sql_result["pieceTitle"][0]
        p_con=sql_result["content"][0]
        l_name=sql_result["legislationName"][0]
        l_index=str(sql_result["legislationIndex"][0])
        p_index = str(sql_result["pieceIndex"][0])


        self.pieceTitle = p_title
        self.content = p_con
        self.legislationName = l_name
        self.legislationIndex = l_index
        self.pieceIndex = p_index


class serializer(JSONEncoder):
    def default(self, o):
        return o.__dict__
#
# @app.route('/search<legIndex>')
# @app.route('/search<cat>')
# @app.route('/simplify_piece<pieceIndex>')
# @app.route('/simplify_leg<legIndex>')



@app.route('/search<query>')
# , methods=['GET', 'POST']
def result(query):
    return_json_answer = json.dumps("No place information is given")
    # query = "what are my human rights?"
    if query != None:
        C = Classifier()
        queryCategory = C.get_category_of_text(query)

        E = Extractor(queryCategory)
        piece_indexes = E.get_ranked_documents("my human rights")

        five_doc_content = []

        host = "classified-legislation.cfb1te3o5nxb.ap-south-1.rds.amazonaws.com"
        port = 3306
        dbname = "classify-legislation"
        user = "admin"
        password = "legalLankan2020"
        conn = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname)

        for element in piece_indexes:
            temp = {}
            sql = '''select p.pieceIndex, p.pieceTitle, p.content, l.legislationIndex, l.legislationName
               from piece p, legislation l
               where p.pieceIndex=''' + element + " and l.legislationIndex=p.legislationIndex;"

            sql_result = pd.read_sql(sql, con=conn)

            Q = QueryAnswer(sql_result)
            JSONData = json.dumps(Q, indent=4, cls=serializer)
            five_doc_content.append(JSONData)


        return_json_answer =  json.dumps(five_doc_content)


    return return_json_answer


if __name__ == '__main__':
    app.run(debug=True)



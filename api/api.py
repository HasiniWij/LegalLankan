import pandas as pd
import pymysql
import json
from flask import Flask
from json import JSONEncoder

from flask import jsonify
from flask_cors import CORS  # comment this on deployment

from dataScienceComponents.Simplifier import Simplifier
from dataScienceComponents.classification.Classifier import Classifier
from dataScienceComponents.extraction.Extractor import Extractor

app = Flask(__name__)

CORS(app)  # comment this on deployment

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

    def to_string(self):
        return self.pieceIndex, self.pieceTitle, self.legislationIndex, self.legislationName, self.content


class serializer(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Legislation():
    def __init__(self, p_title, p_con):
        self.pieceTitle = p_title
        self.content = p_con


@app.route('/legislation/<legIndex>')
def get_legislation(legIndex):
    host = "classified-legislation.cfb1te3o5nxb.ap-south-1.rds.amazonaws.com"
    port = 3306
    dbname = "classify-legislation"
    user = "admin"
    password = "legalLankan2020"
    conn = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname)

    sql = '''select pieceTitle, content
                   from piece where legislationIndex = ''' + str(legIndex)

    sql_result = pd.read_sql(sql, con=conn)

    print(sql_result)

    legislation = []

    for index, row in sql_result.iterrows():
        piece = {"pieceTitle": "", "content": ""}

        pieceTitle = row['pieceTitle']
        content = row['content']

        piece["pieceTitle"] = pieceTitle
        piece["content"] = content

        # L = Legislation(pieceTitle, content)
        # JSONData = json.dumps(L, indent=4, cls=serializer)
        # data.append(JSONData)

        legislation.append(piece)

    # return_json_answer = json.dumps(data)

    return jsonify(legislation)


class LegislationName():
    def __init__(self, l_name, l_index):

        self.legislationName = l_name
        self.legislationIndex = str (l_index)

@app.route('/legistlationlist/<catIndex>')
def get_legislation_list(catIndex):
    host = "classified-legislation.cfb1te3o5nxb.ap-south-1.rds.amazonaws.com"
    port = 3306
    dbname = "classify-legislation"
    user = "admin"
    password = "legalLankan2020"
    conn = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname)

    catIndex = catIndex.strip("<>")

    sql = '''select l.legislationIndex, l.legislationName from legislation l where categoryIndex = ''' + str(catIndex)

    # cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))

    # print(type(categoryIndex))

    sql_result = pd.read_sql(sql , con=conn)

    print(sql_result)

    leg_list = []
    for index, row in sql_result.iterrows():
        leg = {"legislationName": "", "legislationIndex": ""}

        # L = LegislationName(legName, legIndex)
        # JSONData = json.dumps(L, indent=4, cls=serializer)

        legName = row['legislationName']
        legIndex = row['legislationIndex']

        leg["legislationName"] = legName
        leg["legislationIndex"] = legIndex

        leg_list.append(leg)

    # return_json_answer =  json.dumps(data)

    return jsonify(leg_list)


@app.route('/simplifiedpiece/<pieceIndex>')
def get_simplified_piece(pieceIndex):

    host = "classified-legislation.cfb1te3o5nxb.ap-south-1.rds.amazonaws.com"
    port = 3306
    dbname = "classify-legislation"
    user = "admin"
    password = "legalLankan2020"
    conn = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname)

    sql = '''select pieceTitle, content
               from piece 
               where pieceIndex= ''' + str(pieceIndex)

    sql_result = pd.read_sql(sql, con=conn)

    p_title = sql_result["pieceTitle"][0]
    p_con = sql_result["content"][0]

    S = Simplifier()
    lex_simplified = S.get_lexically_simplified_text(p_title + p_con)
    simplified = S.get_syntactically_simplified_text(lex_simplified)

    return_json_answer = json.dumps(simplified)

    return return_json_answer


@app.route('/simplifiedleg/<legIndex>')
def get_simplified_legislation(legIndex):
    host = "classified-legislation.cfb1te3o5nxb.ap-south-1.rds.amazonaws.com"
    port = 3306
    dbname = "classify-legislation"
    user = "admin"
    password = "legalLankan2020"
    conn = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname)

    sql = '''select p.pieceTitle, p.content
               from piece 
               where legistationIndex = ''' + str(legIndex)

    sql_result = pd.read_sql(sql, con=conn)

    data = []
    for index, row in sql_result.iterrows():
        pieceTitle = row['pieceTitle']
        content = row['content']
        S = Simplifier()
        lex_simplified = S.get_lexically_simplified_text(pieceTitle + content)
        simplified = S.get_syntactically_simplified_text(lex_simplified)
        data.append(simplified)

    return_json_answer = json.dumps(data)

    return return_json_answer


@app.route('/search/<query>')
# , methods=['GET', 'POST']
def get_answers(query):

    return_json_answer = json.dumps("No place information is given")
    # query = "what are my human rights?"
    if query != None:
        C = Classifier()
        queryCategory = C.get_category_of_text(query)

        E = Extractor(queryCategory)
        piece_indexes = E.get_ranked_documents(C.get_query_keywords(query))

        # five_doc_content = []

        host = "classified-legislation.cfb1te3o5nxb.ap-south-1.rds.amazonaws.com"
        port = 3306
        dbname = "classify-legislation"
        user = "admin"
        password = "legalLankan2020"
        conn = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname)

        answers = []

        for element in piece_indexes:
            temp = {}
            sql = '''select p.pieceIndex, p.pieceTitle, p.content, l.legislationIndex, l.legislationName
               from piece p, legislation l
               where p.pieceIndex=''' + str(element) + " and l.legislationIndex=p.legislationIndex;"

            sql_result = pd.read_sql(sql, con=conn)

            # Q = QueryAnswer(sql_result)
            # print(Q.to_string())

            answer = {"pieceTitle": "", "content": "", "legislationName": "", "legislationIndex": "", "pieceIndex": ""}
            p_title = sql_result["pieceTitle"][0]
            p_con = sql_result["content"][0]
            l_name = sql_result["legislationName"][0]
            l_index = str(sql_result["legislationIndex"][0])
            p_index = str(sql_result["pieceIndex"][0])

            answer["pieceTitle"] = p_title
            answer["content"] = p_con
            answer["legislationName"] = l_name
            answer["legislationIndex"] = l_index
            answer["pieceIndex"] = p_index

            answers.append(answer)

            # JSONData = json.dumps(Q, indent=4, cls=serializer)
            # five_doc_content.append(JSONData)

        # return_json_answer = json.dumps(five_doc_content)

    return jsonify(answers)


if __name__ == '__main__':
    app.run(debug=True)



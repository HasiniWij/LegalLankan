import pandas as pd
import pymysql
import json
from flask import Flask, request, url_for, redirect
from flask import jsonify
from flask_cors import CORS  # comment this on deployment

from dataScienceComponents.Simplifier import Simplifier
from dataScienceComponents.classification.Classifier import Classifier
from dataScienceComponents.extraction.Extractor import Extractor

app = Flask(__name__)

CORS(app)  # comment this on deployment


def database(database_name="classify-legislation"):
    host = "classified-legislation.cfb1te3o5nxb.ap-south-1.rds.amazonaws.com"
    port = 3306
    dbname = database_name
    user = "admin"
    password = "legalLankan2020"
    conn = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname)
    return conn


@app.route('/legislation/<legIndex>')
def get_legislation(legIndex):
    conn = database()

    sql = '''select pieceTitle, content
                   from piece where legislationIndex = ''' + str(legIndex)

    sql_result = pd.read_sql(sql, con=conn)

    legislation = []

    for index, row in sql_result.iterrows():
        piece = {"pieceTitle": "", "content": ""}
        pieceTitle = row['pieceTitle']
        content = row['content']
        piece["pieceTitle"] = pieceTitle
        piece["content"] = content
        legislation.append(piece)

    return jsonify(legislation)


@app.route('/legistlationlist/<catIndex>')
def get_legislation_list(catIndex):
    conn = database()
    catIndex = catIndex.strip("<>")
    sql = '''select l.legislationIndex, l.legislationName from legislation l where categoryIndex = ''' + '"' + str(
        catIndex) + '"'
    sql_result = pd.read_sql(sql, con=conn)

    leg_list = []
    for index, row in sql_result.iterrows():
        leg = {"legislationName": "", "legislationIndex": ""}
        legName = row['legislationName']
        legIndex = row['legislationIndex']

        leg["legislationName"] = legName
        leg["legislationIndex"] = legIndex

        leg_list.append(leg)
    return jsonify(leg_list)


@app.route('/simplifiedpiece/<pieceIndex>')
def get_simplified_piece(pieceIndex):
    conn = database()

    sql = '''select pieceTitle, content
               from piece 
               where pieceIndex= ''' + str(pieceIndex)

    sql_result = pd.read_sql(sql, con=conn)

    p_title = sql_result["pieceTitle"][0]
    p_con = sql_result["content"][0]

    piece = [p_title, p_con]

    S = Simplifier()
    lex_simplified = S.get_lexically_simplified_text(piece)
    simplified = S.get_syntactically_simplified_text(lex_simplified)
    answer = {"pieceTitle": "", "content": ""}
    print(simplified)
    answer["pieceTitle"] = simplified[0][0]
    if len(simplified[0]) == 3:
        answer["content"] = simplified[0][1] + ". " + simplified[0][2]
    else:
        answer["content"] = simplified[0][1]

    return jsonify(answer)


@app.route('/simplifiedleg/<legIndex>')
def get_simplified_legislation(legIndex):
    conn = database()

    sql = '''select pieceTitle, content
               from piece
               where legislationIndex = ''' + str(legIndex)

    sql_result = pd.read_sql(sql, con=conn)

    data = []
    for index, row in sql_result.iterrows():
        pieceTitle = row['pieceTitle']
        content = row['content']
        data.append(pieceTitle)
        data.append(content)

    S = Simplifier()
    lex_simplified = S.get_lexically_simplified_text(data)
    simplified = S.get_syntactically_simplified_text(lex_simplified)
    data = []
    for i in range(0, len(simplified), 2):
        answer = {"pieceTitle": "", "content": ""}
        answer["pieceTitle"] = simplified[i]
        answer["content"] = simplified[i + 1]
        data.append(answer)
    return jsonify(data)


@app.route('/search/<query>')
def get_answers(query):
    if query != None:
        C = Classifier()
        queryCategory = C.get_category_of_text(query)

        E = Extractor(queryCategory)
        piece_indexes = E.get_ranked_documents(C.get_query_keywords(query))

        conn = database()

        answers = []
        for element in piece_indexes:
            temp = {}
            sql = '''select p.pieceIndex, p.pieceTitle, p.content, l.legislationIndex, l.legislationName
               from piece p, legislation l
               where p.pieceIndex=''' + str(element) + " and l.legislationIndex=p.legislationIndex;"

            sql_result = pd.read_sql(sql, con=conn)

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

    return jsonify(answers)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userName = request.form['userName']
        adminPassword = request.form['password']
        conn = database("admins")
        sql = '''select adminPassword from account_info where adminUsername=''' + "'" + str(userName) + "'"
        sql_result = pd.read_sql(sql, con=conn)

        if sql_result.empty:
            result = "Invalid username"

        elif sql_result["adminPassword"][0] == adminPassword:
            result = "Signing in..."
        else:
            result = "Invalid details"

        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

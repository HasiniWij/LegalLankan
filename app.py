import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

from flask import Flask, jsonify, request
from backend.DatabaseConnection import DatabaseConnection
from dataScienceComponents.classification.Classifier import Classifier
from dataScienceComponents.extraction.Extractor import Extractor
from dataScienceComponents.simplification.Simplifier import Simplifier


app = Flask(__name__)


@app.route('/')
def default():
    return "LegalLankan API"


@app.route('/legislation/<legIndex>')
def get_legislation(legIndex):
    sql = '''select pieceTitle, pieceIndex, content from piece where legislationIndex = ''' + str(legIndex)

    db = DatabaseConnection("classify-legislation")
    sql_result = db.selectFromDB(sql)

    legislation = []

    for index, row in sql_result.iterrows():
        piece = {"pieceTitle": "", "content": "","number":"", "pieceIndex":""}
        
        piece["content"] = row['content']
        piece["pieceIndex"] = row['pieceIndex']
        
        pieceTitle = row['pieceTitle']
        temp = pieceTitle.split("-", 1)
        piece["pieceTitle"] = temp[1]
        piece["number"] = int(temp[0])
        
        legislation.append(piece)
        
        
    legislation.sort(key=lambda item: item.get("number"))
    for item in legislation:
        item.pop("number")
    return jsonify(legislation)
    
@app.route('/legislationlist/<catIndex>')
def get_legislation_list(catIndex):
    catIndex = catIndex.strip("<>")
    sql = '''select l.legislationIndex, l.legislationName from legislation l where categoryIndex = ''' + '"' + str(
        catIndex) + '"'
    db = DatabaseConnection("classify-legislation")
    sql_result = db.selectFromDB(sql)
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
    print("piece index "+pieceIndex)
    sql = '''select pieceTitle, content from piece where pieceIndex= ''' + str(pieceIndex)

    db = DatabaseConnection("classify-legislation")
    sql_result = db.selectFromDB(sql)

    p_title = sql_result["pieceTitle"][0]
    temp = p_title.split("-", 1)
    p_title = temp[1]
    p_con = sql_result["content"][0]

    piece = [p_title, p_con]

    S = Simplifier()
    lex_simplified = S.get_lexically_simplified_text(piece)
    simplified = S.get_syntactically_simplified_text(lex_simplified)
    answer = {"pieceTitle": "", "content": "", "pieceIndex": pieceIndex}
    answer["pieceTitle"] = simplified[0]
    if len(simplified) == 3:
        answer["content"] = simplified[1] + ". " + simplified[2]
    else:
        answer["content"] = simplified[1]

    return jsonify(answer)


@app.route('/search/<query>')
def get_answers(query):
    if query is not None:
        C = Classifier("dataScienceComponents/classification/models/svm.pickle", "dataScienceComponents"
                                                                                    "/classification/models/tfidf"
                                                                                    ".pickle")
        query_category = C.get_category_of_text(query)

        E = Extractor(query_category)
        piece_indexes = E.get_ranked_documents(C.get_query_keywords(query))

        answers = []
        for element in piece_indexes:
            sql = '''select p.pieceIndex, p.pieceTitle, p.content, l.legislationIndex, l.legislationName
               from piece p, legislation l
               where p.pieceIndex=''' + str(element) + " and l.legislationIndex=p.legislationIndex;"

            db = DatabaseConnection("classify-legislation")
            sql_result = db.selectFromDB(sql)

            answer = {"pieceTitle": "", "content": "", "legislationName": "", "legislationIndex": "", "pieceIndex": ""}
            p_title = sql_result["pieceTitle"][0]
            p_con = sql_result["content"][0]
            l_name = sql_result["legislationName"][0]
            l_index = str(sql_result["legislationIndex"][0])
            p_index = str(sql_result["pieceIndex"][0])

            
            temp = p_title.split("-", 1)
            p_title = temp[1]
            
            answer["pieceTitle"] = p_title
            answer["content"] = p_con
            answer["legislationName"] = l_name
            answer["legislationIndex"] = l_index
            answer["pieceIndex"] = p_index

            answers.append(answer)

    return jsonify(answers)


@app.route('/login')
def login():
    if request.method == 'POST':
        data=request.json
        user_name = data.get('userName')
        admin_password = data.get('password')

        sql = '''select adminPassword from account_info where adminUsername=''' + "'" + str(user_name) + "'"
        db = DatabaseConnection("admins")
        sql_result = db.selectFromDB(sql)

        if sql_result.empty:
            result = "Invalid username"

        elif sql_result["adminPassword"][0] == admin_password:
            result = "Signing in..."
        else:
            result = "Invalid details"

        return result


# @app.route('/uploadLeg')
# def uploadLegislation():
#     global piece_title
#     if request.method == 'POST':
#         db = DatabaseConnection("classify-legislation")
#         legislation = request.form['legislation']
#         legislation_name = request.form['legislation_name']
#
#         insert_leg_sql = "INSERT INTO legislation ( legislationName) VALUES (%s)"
#         val = (legislation_name)
#         db.insertToDB(insert_leg_sql, val)
#

#         splitter = DocumentSplitting()
#         list_dictionary_piece = splitter.getpieces(legislation)

#         splitter = DocumentSplitter()
#         list_dictionary_piece = splitter.split_core_legislation(legislation)

#
#         sql = "select legislationIndex from legislation where legislationName=" + legislation_name
#         sql_result = db.selectFromDB(sql)
#         leg_index = sql_result["legislationName"][0]
#
#         categories = {}
#         # article1:CR,article2=CR,
#         for piece_dictionary in list_dictionary_piece:
#             C = Classifier()
#             piece_category = C.get_category_of_text(piece_title + piece_dictionary.get(piece_title))
#             categories[piece_title] = piece_category
#
#         same_category = len(list(set(list(categories.values())))) == 1
#
#         if same_category:
#             cat=categories[0].get(piece_title)
#             update_leg_category_sql = "UPDATE legislation SET categoryIndex = "+str(cat)+" WHERE legislationIndex =" +leg_index
#             db.updateDB(update_leg_category_sql)
#             for piece_dictionary in list_dictionary_piece:
#                 sql = "INSERT INTO piece ( pieceTitle,content,legislationIndex) VALUES (%s, %s,%s)"
#                 val = (piece_title, piece_dictionary.get(piece_title),leg_index)
#                 db.insertToDB(sql, val)
#
#         else:
#             for piece_dictionary in list_dictionary_piece:
#                 sql = "INSERT INTO pieceCategory ( pieceTitle,content,legislationIndex,categoryIndex) VALUES (%s, %s,%s,%s)"
#                 val = (piece_title, piece_dictionary.get(piece_title), leg_index,categories.get(piece_title))
#                 db.insertToDB(sql, val)


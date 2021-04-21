import nltk  # used for NLP

nltk.download('wordnet')  # Used for lemmatization
nltk.download('stopwords')  # used to remove stopwords
nltk.download('punkt')  # used tokenize sentences

from flask import Flask, jsonify, request  # to provide an API (Handle requests, turn objects to json)
from backend.DatabaseConnection import DatabaseConnection  # used to connect and perform operation on database
from backend.UploadLeg import UploadLeg  # used to upload legislation to system
from dataScienceComponents.classification.Classifier import Classifier  # Used for classification
from dataScienceComponents.extraction.Extractor import Extractor  # used for Extraction
from dataScienceComponents.simplification.Simplifier import Simplifier  # used for simplification

app = Flask(__name__)


@app.route('/')
def default():
    return "LegalLankan API"


@app.route('/legislation/<legIndex>')
def get_legislation(legIndex):
    # select all the pieces of the legislation
    sql = '''select pieceTitle, pieceIndex, content from piece where legislationIndex = ''' + str(legIndex)
    db = DatabaseConnection("classify-legislation")
    sql_result = db.selectFromDB(sql)

    legislation = []
    for index, row in sql_result.iterrows():
        piece = {"pieceTitle": "", "content": "", "number": "", "pieceIndex": ""}

        piece["content"] = row['content']
        piece["pieceIndex"] = row['pieceIndex']

        pieceTitle = row['pieceTitle']
        temp = pieceTitle.split("-", 1)
        piece["pieceTitle"] = temp[1]
        piece["number"] = int(temp[0])

        legislation.append(piece)

    # Putting the pieces into the right order
    legislation.sort(key=lambda item: item.get("number"))
    for item in legislation:
        item.pop("number")

    return jsonify(legislation)


@app.route('/legislationlist/<catIndex>')
def get_legislation_list(catIndex):
    catIndex = catIndex.strip("<>")

    # Select al legislation of the category
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

    # Extract the piece
    sql = '''select pieceTitle, content from piece where pieceIndex= ''' + str(pieceIndex)
    db = DatabaseConnection("classify-legislation")
    sql_result = db.selectFromDB(sql)

    p_title = sql_result["pieceTitle"][0]
    temp = p_title.split("-", 1)
    p_title = temp[1]
    p_con = sql_result["content"][0]

    piece = [p_title, p_con]

    # Simplify the piece
    S = Simplifier()
    lex_simplified = S.get_lexically_simplified_text(piece)
    simplified = S.get_syntactically_simplified_text(lex_simplified)

    answer = {"pieceTitle": simplified[0], "content": "", "pieceIndex": pieceIndex}
    if len(simplified) == 3:
        answer["content"] = simplified[1] + ". " + simplified[2]
    else:
        answer["content"] = simplified[1]

    return jsonify(answer)


@app.route('/search/<query>')
def get_answers(query):
    if query is not None:

        # Classify the query
        C = Classifier("dataScienceComponents/classification/models/svm.pickle", "dataScienceComponents"
                                                                                 "/classification/models/tfidf"
                                                                                 ".pickle")
        query_category = C.get_category_of_text(query)

        # extract pieces relevant to query
        E = Extractor(query_category)
        piece_indexes = E.get_ranked_documents(C.get_query_keywords(query))

        # extract all info of the pieces relevant to query
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
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

        return jsonify(result)


@app.route('/uploadLeg', methods=['GET', 'POST'])
def uploadLegislation():
    if request.method == 'POST':
        data = request.json
        text = data.get('text')
        u = UploadLeg()
        u.upload_data_of_piece(text)

        return jsonify("successfully uploaded")

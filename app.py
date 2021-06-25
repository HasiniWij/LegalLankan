import pickle
import re
from nltk.tokenize import sent_tokenize
import nltk  # used for NLP

# nltk.download('wordnet')  # Used for lemmatization
# nltk.download('stopwords')  # used to remove stopwords
# nltk.download('punkt')  # used tokenize sentences

from flask import Flask, jsonify, request  # to provide an API (Handle requests, turn objects to json)

from backend.UploadLeg import UploadLeg
from dataScienceComponents.extraction.Extractor import Extractor  # used for Extraction
from dataScienceComponents.simplification.Simplifier import Simplifier  # used for simplification
from flask_cors import CORS   # comment this on deployment

app = Flask(__name__)
CORS(app)  # comment this on deployment


@app.route('/')
def default():
    return "LegalLankan API"


@app.route('/legislation/<legName>')
def get_legislation(legName):

    global block_result
    with open("data.pickle", 'rb') as data:
        data = pickle.load(data)

    content=""
    for index, row in data.iterrows():
        if row['title']==legName:
            content=row['content']

    S = Simplifier()
    complex_words = S.identify_complex_words(content)

    list_of_blocks=[]
    block = ""
    content = content.replace("\n", "")
    f = sent_tokenize(content)
    block_result = {"title": "", "content": ""}
    previous_line=""
    for line in f:

        x = line.replace(".", "")
        if x.isdecimal():

            block = block.replace(previous_line, "")
            block_result["content"]=block
            list_of_blocks.append(block_result)
            block_result = {"title": line+previous_line, "content": ""}
            block=""
        else:
            block=block+line

        previous_line=line
        
    if len(list_of_blocks)==0:
        block_result = {"title": "", "content": content}
        list_of_blocks.append(block_result)
  
    result={'complexWords':complex_words,"block":list_of_blocks}

    return jsonify(result)


@app.route('/legislationlist/<category>')
def get_legislation_list(category):

    legislationlist=[]

    with open("title_category.pickle", 'rb') as legislation_list:
        legislation_list = pickle.load(legislation_list)

    for index, row in legislation_list.iterrows():

        if row['category']==category:
            leg={'title': row['title']}
            legislationlist.append(leg)


    return jsonify(legislationlist)


@app.route('/simplifiedWord/<word>/<sentence>')
def get_simplified_piece(word,sentence):
    S=Simplifier()
    words=S.get_bert_candidates(sentence,word)

    result=''
    isFirst=True
    count=1
    for i in words:

        if count==4:
            break

        if i==word:
            continue

        elif isFirst:
            result=i
            isFirst=False
            count+=1
        else:
            result=result+", "+i
            count+=1

    return jsonify(result)


@app.route('/search/<query>')
def get_answers(query):
    if query is not None:
        E = Extractor()
        result = E.get_ranked_documents(E.get_query_keywords(query))
        return jsonify(result)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        user_name = data.get('userName')
        admin_password = data.get('password')

        if user_name=="admin1" and admin_password=="123":
            result = "Signing in..."

        else:
            result = "Invalid details entered! "

        return jsonify(result)


@app.route('/uploadLeg', methods=['GET', 'POST'])
def uploadLegislation():
    if request.method == 'POST':
        data = request.json
        text = data.get('text')
        title=data.get('title')

        text = text.replace("\r", "")
        title=title.replace("\r", "")

        u = UploadLeg()

        if data.get('type')=="core":        
            u.upload_core_leg(text)
            
        else:
            u.upload_act(text,title [0:-4])

        return jsonify("successfully uploaded")
from flask import Flask, request
from classification.Classifier import Classifier
# from .Classifier import get_query_keywords
from extraction.Extractor import Extractor

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return{
#         'name':'Hello world'
#     } 

@app.route('/search', methods = ['GET', 'POST'])
def result():
    if request.method == 'GET':
        query = request.args.get('query', None)
        if query:
            C = Classifier("/Users/Shontaal/Documents/GitHub/SDGP/api/classification/models/best_rfc.pickle", "/Users/Shontaal/Documents/GitHub/SDGP/api/classification/models/tfidf.pickle")
            queryCategory = C.get_category_of_text(query)

            E = Extractor(queryCategory)
            extracted = E.get_ranked_documents("main human rights")

            listToStr = ' '.join(map(str, extracted)) 
            print("Query: " + query + '\n' + "Query Category: " + queryCategory + '\n' + "Extraction Piece Index: " + listToStr)
            return "Query: " + query + " ||| " + "Query Category: " + queryCategory + " ||| " + "Extraction Piece Index: " + listToStr

        return "No place information is given"


if __name__ == '__main__':
    app.run(debug=True)
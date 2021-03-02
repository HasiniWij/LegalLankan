from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return{
        'name': 'Hello World'
    } 

@app.route('/search', methods = ['GET', 'POST'])
def result():
    if request.method == 'GET':
        query = request.args.get('query', None)
        if query:
            return query
        return "No place information is given"

if __name__ == '__main__':
    app.run(debug=True)
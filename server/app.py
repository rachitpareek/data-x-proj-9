import json
import pickle
from util import *
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, redirect, url_for, make_response

# start flask
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# render default webpage
@app.route('/', methods=['GET', 'POST'])
def home():

    data = {}

    print("was there any data?")
    if request.data:
        print("RECEIVED DATA:")
        print(request.data)
        data = json.loads(request.data)
    
    with open("./resources/model.pkl", 'rb') as file:
        model = pickle.load(file)

    with open("./resources/vectorizer.pkl", 'rb') as file:
        vectorizer = pickle.load(file)

    if "message" not in data:
        data["message"] = "Space lasers cause forest fires"

    output = model.predict(vectorizer.transform([data["message"]]))
    
    print(output)

    return str(output)

# render default webpage
@app.route('/test')
def test():
    return "TEST"

# render default webpage
@app.route('/extension')
def extension():
    return render_template('extension.html')

# # render default webpage
# @app.route('/')
# def home():
#     return render_template('home.html')

@app.after_request
def after_request_func(response):
    response.direct_passthrough = False
    print(response.get_data())
    origin = request.headers.get('Origin')
    response = make_response(response)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

app.run(debug=True)

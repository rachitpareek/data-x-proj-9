from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_cors import CORS, cross_origin

import json

# start flask
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# render default webpage
@app.route('/', methods=['GET', 'POST'])
def home():
    
    data = json.loads(request.data)
    print("RECEIVED DATA:")
    print(data)

    return render_template('home.html')

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

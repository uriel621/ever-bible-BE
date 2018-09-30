from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def all_bible():
    # url = "https://api.scripture.api.bible/v1/bibles"
    # headers = {'Content-Type':'application/x-www-form-urlencoded', 'api-key': '81f316c5f31960d155555818b8d0a59c'}
    # response = requests.request("GET", url, headers=headers)
    # return response.json()
    url = "https://raw.githubusercontent.com/honza/bibles/master/NIV/NIV.json"
    response = requests.request("GET", url)
    return response.json()

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify(all_bible())

if __name__ == '__main__':
    app.run(debug=True)
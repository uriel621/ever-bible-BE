from flask import Flask, jsonify
import requests

app = Flask(__name__)

def all_bible():
    url = "https://api.scripture.api.bible/v1/bibles"
    headers = {'Content-Type':'application/x-www-form-urlencoded', 'api-key': '81f316c5f31960d155555818b8d0a59c'}
    response = requests.request("GET", url, headers=headers)
    return response.json()

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify(all_bible())

if __name__ == '__main__':
    app.run(debug=True)
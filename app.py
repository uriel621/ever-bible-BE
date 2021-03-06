from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

from books.books import books

app = Flask(__name__, static_url_path='/static')
CORS(app)

# import sys
# print(sys.modules)
# print('@books', books)
def all_bible():
    # url = "https://api.scripture.api.bible/v1/bibles"
    # headers = {'Content-Type':'application/x-www-form-urlencoded', 'api-key': '81f316c5f31960d155555818b8d0a59c'}
    # response = requests.request("GET", url, headers=headers)
    # return response.json()
    url = "https://raw.githubusercontent.com/honza/bibles/master/NIV/NIV.json"
    response = requests.request("GET", url)
    return response.json()

all_biblex = all_bible()

@app.route('/', methods=['GET'])
def get_tasks():
    book_list = books
    counter = 0
    for book in book_list:
        counter = counter + 1
        book['id'] = counter
        book['location'] = '{}{}'.format(request.base_url, book['img'])
    
    return jsonify(book_list)

@app.route('/chapter/<chapter>', methods=['GET'])
def get_chapters(chapter):
    # chapter = chapter[0].upper()+chapter[1:]
    # all_biblex = all_bible()
    chapter = all_biblex[chapter]
    return jsonify(len(chapter))

@app.route('/book/<book>/chapter/<chapter>', methods=['GET'])
def get_chapter(book, chapter):
    # chapter = chapter[0].upper()+chapter[1:]
    # all_biblex = all_bible()
    book = all_biblex[book][chapter]
    return jsonify(book)

if __name__ == '__main__':
    app.run()

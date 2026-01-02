from app import app
from flask import request, jsonify
from search_engine_func.search_by_words import search_wordlist

@app.route("/search", methods=["POST"])
def search():
    wordslist = request.json["searchString"].split()

    search_result_list = search_wordlist(wordslist)
    

    return jsonify(search_result_list)

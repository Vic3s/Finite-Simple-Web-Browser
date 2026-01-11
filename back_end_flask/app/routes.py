from flask_cors import cross_origin
from . import app
from flask import request, jsonify
from search_engine_func.search_by_words import get_wordlist, search_
from flask import Response
from bson import json_util

@app.route("/search", methods=["POST"])
@cross_origin()
def search():
    wordslist = request.json["searchString"].split()

    results_object_list = json_util.dumps(search_(get_wordlist(wordslist)))

    # for result_object in results_object_list:
    #     result_object.pop("_id")


    return Response(results_object_list, mimetype="application/json")


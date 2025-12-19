from app import app
from flask import request, jsonify
from flask_cors import CORS

CORS(app)

@app.route("/search")
def search():
    print(request.form)

    return jsonify({
        "message": "Search successfull",
        "status": 200
    })

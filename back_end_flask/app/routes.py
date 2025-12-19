from app import app
from flask import render_template

@app.route("/search")
def search():
    return "test"

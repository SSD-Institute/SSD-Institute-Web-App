from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/collaborative-veto")
def collaborative_veto():
    return render_template('collaborative-veto.html')

@app.route("/supreme-court-check")
def supreme_court_check():
    return render_template('supreme-court-check.html')

@app.route("/multiple-choice-voting")
def multiple_choice_voting():
    return render_template('multiple-choice-voting.html')

@app.route("/minimum-space")
def minimum_space():
    return render_template('minimum-space.html')
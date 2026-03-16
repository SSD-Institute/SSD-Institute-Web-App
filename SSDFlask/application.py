import os

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        'base.html',
        title = "Scientific Self Determination",
        stylesheet = "home.css",
        page_content = render_template("home.html")
    )

@app.route("/collaborative-veto")
def collaborative_veto():
    return render_template(
        'base.html',
        title = 'Collaborative Veto',
        stylesheet="collaborative_veto.css",
        page_content = render_template('collaborative-veto.html')
    )

@app.route("/supreme-court-check")
def supreme_court_check():
    scv_path = os.path.join(app.root_path, "static", "visualizations", "scv")
    return render_template(
        'base.html',
        title = 'Supreme Court Check',
        stylesheet="supreme_court_check.css",
        scripts=["/static/scripts/SupremeCourtVetoSwitcher.js"],
        page_content=render_template(
            'supreme-court-check.html',
            visualization_paths=sorted(
                f for f in os.listdir(scv_path)
                    if f.endswith(".html")
            )
        )
    )

@app.route("/multiple-choice-voting")
def multiple_choice_voting():
    mcv_path = os.path.join(app.root_path, "static", "visualizations", "mcv")
    return render_template(
        'base.html',
        title='Multiple Choice Voting',
        stylesheet="multiple_choice_voting.css",
        scripts=["/static/scripts/ApprovalVotingSwitcher.js"],
        page_content=render_template(
            'multiple-choice-voting.html',
            visualization_paths=sorted(
                f for f in os.listdir(mcv_path)
                    if f.endswith(".html")
            )
        )
    )

@app.route("/minimum-space")
def minimum_space():
    return render_template(
        'base.html',
        title = 'Minimum Amount of Space',
        stylesheet="minimum_space.css",
        page_content = render_template('minimum-space.html')
    )

@app.route("/contact")
def contact():
    return render_template(
        'base.html',
        title = 'Contact Us',
        stylesheet="contact.css",
        page_content = render_template('contact.html')
    )
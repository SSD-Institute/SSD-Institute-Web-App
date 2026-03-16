import os
import plotly.express as px
import pandas as pd
from data.sample import ApprovalVotingData

# Resolve project root based on this file's location
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to static visualization directory
OUTPUT_DIR = os.path.join(
    PROJECT_ROOT,
    "..", # Traverse out of the `visualization_scripts`` subdirectory
    "static",
    "visualizations",
    "mcv"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

for election_title, election in ApprovalVotingData.elections.items():

    voting_methods = []
    candidates = []
    vote_totals = []

    for voting_method, results in election.items():
        for candidate, vote_total in results.items():
            voting_methods.append(voting_method)
            candidates.append(candidate)
            vote_totals.append(vote_total)

    df = pd.DataFrame({
        "Voting Method": voting_methods,
        "Candidate": candidates,
        "Vote Totals": vote_totals
    })

    fig = px.bar(
        df,
        x="Voting Method",
        y="Vote Totals",
        color="Candidate",
        barmode="group",
        title=election_title
    )

    filename = election_title.lower().replace(" ", "-") + ".html"
    output_path = os.path.join(OUTPUT_DIR, filename)

    fig.write_html(output_path)
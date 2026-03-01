import plotly.express as px
import pandas as pd

from data.sample import ApprovalVotingData

for election_title, election in ApprovalVotingData.elections.items():

    voting_methods = list()
    candidates = list()
    vote_totals = list()

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

    fig.write_html("/static/visualizations/mcv/" + election_title.lower().replace(" ", "-") + ".html")
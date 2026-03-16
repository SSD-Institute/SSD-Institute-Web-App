import os
import pandas as pd
import plotly.express as px

from data.sample import SupremeCourtCheckData

# Resolve project root based on this file's location
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to static visualization directory
OUTPUT_DIR = os.path.join(
    PROJECT_ROOT,
    "..", # Traverse out of the `visualization_scripts`` subdirectory
    "static",
    "visualizations",
    "scv"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

for decision, policies in SupremeCourtCheckData.SupremeCourtCheckData.items():

    policy_list = list()
    state_list = list()
    
    for policy, states in policies.items():
        for state in states:
            state_list.append(state)
            policy_list.append(policy)

    data = {
        "states": state_list,
        "value": policy_list
    }

    df = pd.DataFrame(data)

    # Define colors
    color_map = {
        "Override Supreme Court Decision": "red",
        "Support Supreme Court Decision": "green",
        "Mixed / Independent Policy": "yellow",
        "Not a State Yet": "lightgray"
    }

    fig = px.choropleth(
        df,
        locations="states",
        locationmode="USA-states",
        color="value",
        scope="usa",
        color_discrete_map=color_map,
    )

    fig.update_layout(
        title=decision,
        legend_title="Status"
    )

    filename = decision.lower().replace(" ", "-") + ".html"
    output_path = os.path.join(OUTPUT_DIR, filename)

    fig.write_html(output_path)
import os
import pandas as pd
import plotly.express as px
import json

from data.sample import CollabVetoData

# Resolve project root based on this file's location
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to static visualization directory
OUTPUT_DIR = os.path.join(
    PROJECT_ROOT,
    "..", # Traverse out of the `visualization_scripts`` subdirectory
    "static",
    "visualizations",
    "cv"
)

# GeoJSON path
COUNTIES_GEOJSON_PATH = os.path.join(
    PROJECT_ROOT,
    "data",

    # The GEOJSON is derived from this website: https://eric.clst.org/tech/usgeojson/
    # The file there contains the entire US, so I manually clipped it to just WY.
    # That website, in turn, adapted it from the official US census shapefiles.
    "wy_counties.geojson"
)

with open(COUNTIES_GEOJSON_PATH, "r") as f:
    counties_geojson = json.load(f)

os.makedirs(OUTPUT_DIR, exist_ok=True)

color_map = {
    "Allow": "green",
    "Veto": "red"
}

for title, scenario in CollabVetoData.collaborative_veto_scenarios.items():

    county_list = []
    decision_list = []

    for fips, decision in scenario.items():
        county_list.append(fips)
        decision_list.append(decision)

    # Create DataFrame
    df = pd.DataFrame({
        "fips": county_list,
        "decisions": decision_list
    })

    # Map FIPS → County Name
    df["County"] = df["fips"].map(CollabVetoData.WYOMING_COUNTIES)

    # Map decision → readable label
    df["Decision"] = df["decisions"].map({
        0: "Allow",
        1: "Veto"
    })

    # Split FIPS into STATE + COUNTY (for GeoJSON matching)
    df["STATE"] = df["fips"].str[:2]
    df["COUNTY"] = df["fips"].str[2:].str.zfill(3)

    # Create choropleth
    fig = px.choropleth(
        df,
        geojson=counties_geojson,
        locations="COUNTY",
        color="Decision",
        color_discrete_map=color_map,
        featureidkey="properties.COUNTY",
        scope="usa",
        hover_data={
            "County": True,
            "Decision": True,
            "COUNTY": False,
            "STATE": False,
            "fips": False,
            "decisions": False
        }
    )

    # Fit map to Wyoming counties
    fig.update_geos(fitbounds="locations", visible=False)

    # Clean legend title
    fig.update_layout(
        title=title,
        legend_title_text="Decision"
    )

    filename = title.lower().replace(" ", "-") + ".html"

    output_path = os.path.join(OUTPUT_DIR, filename)

    fig.write_html(output_path)
import os
import pandas as pd
import plotly.express as px

from data.sample import WYCountyData

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Creates path to static visualization directory
OUTPUT_DIR = os.path.join(
   PROJECT_ROOT,
   "..",
   "static",
   "visualizations",
   "wy-county"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

COLOR_MAP = {
   "Federal Dominant": "steelblue",
   "Private Dominant": "forestgreen",
   "Mixed Use": "darkorange",
   "State Trust Land Dominant": "mediumpurple"
}

for scenario_title, county_data in WYCountyData.WYCountyData.items():

   fips_list = []
   classification_list = []

   for fips, classification in county_data.items():
      fips_list.append(fips)
      classification_list.append(classification)

   df = pd.DataFrame({
      "fips": fips_list,
      "classification": classification_list
   })

   fig = px.choropleth(
      df,
      geojson="https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json",
      locations="fips",
      color="classification",
      color_discrete_map=COLOR_MAP,
      scope="usa",
      title=scenario_title
   )

   fig.update_geos(fitbounds="locations", visible=False)
   fig.update_layout(
      title=scenario_title,
      legend_title="Land Classification"
   )

   filename = (
      scenario_title.lower()
      .replace(" ", "-")
      .replace("(", "")
      .replace(")", "")
      .replace("--", "-")
      + ".html"
   )
   output_path = os.path.join(OUTPUT_DIR, filename)

   fig.write_html(output_path)

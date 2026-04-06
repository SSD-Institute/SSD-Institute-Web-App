import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from data.sample import WYCountyData

app = dash.Dash(__name__)

COLOR_MAP = {
   "Federal Dominant": "steelblue",
   "Private Dominant": "forestgreen",
   "Mixed Use": "darkorange",
   "State Trust Land Dominant": "mediumpurple"
}

app.layout = html.Div([
   html.H1("Wyoming County Land Classification Tracker"),
   dcc.Dropdown(
      id='wy-county-dropdown',
      options=[{'label': k, 'value': k} for k in WYCountyData.WYCountyData.keys()],
      value=list(WYCountyData.WYCountyData.keys())[0]
   ),
   dcc.Graph(id='wy-county-choropleth')
])

@app.callback(
   Output('wy-county-choropleth', 'figure'),
   Input('wy-county-dropdown', 'value')
)
def update_graph(selected_scenario):
   county_data = WYCountyData.WYCountyData[selected_scenario]

   fips_list = []
   classification_list = []

   for fips, classification in county_data.items():
      fips_list.append(fips)
      classification_list.append(classification)

   df = pd.DataFrame({"fips": fips_list, "classification": classification_list})

   fig = px.choropleth(
      df,
      geojson="https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json",
      locations="fips",
      color="classification",
      color_discrete_map=COLOR_MAP,
      scope="usa",
      title=selected_scenario
   )

   fig.update_geos(fitbounds="locations", visible=False)
   fig.update_layout(title=selected_scenario, transition_duration=500)
   return fig

if __name__ == '__main__':
   app.run(debug=True)

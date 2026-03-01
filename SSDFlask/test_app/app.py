import dash
from dash import dcc, html, Input, Output, callback, ctx
import plotly.express as px
import pandas as pd
from utils.data_utils import load_election_data, filter_data_by_year


app = dash.Dash(__name__)
server = app.server 

df = load_election_data('election_data.csv')

app.layout = html.Div([
   html.H1("US Presidential Election Results"),
   dcc.Dropdown(
      id='year-selector',
      options=[{'label': y, 'value': y} for y in df['Year'].unique()],
      value='2000'
   ),
   dcc.Graph(id='results-bar-chart'),
   html.Div(id='summary-text')
])

@callback(
   Output('results-bar-chart', 'figure'),
   Output('summary-text', 'children'),
   Input('year-selector', 'value')
)
def update_chart(selected_year):
   if not selected_year:
      return dash.no_update, "Select a year"
    
   filtered_df = filter_data_by_year(df, selected_year)
   fig = px.bar(filtered_df, x="Candidate", y="Votes", color="Method", barmode="group")
    
   msg = f"Showing {selected_year} data. Triggered by: {ctx.triggered_id}"
   return fig, msg

if __name__ == '__main__':
   app.run(debug=True)
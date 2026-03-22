import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from data.sample import SupremeCourtCheckData

app = dash.Dash(__name__)

COLOR_MAP = {
   "Override Supreme Court Decision": "red",
   "Support Supreme Court Decision": "green",
   "Mixed / Independent Policy": "yellow",
   "Not a State Yet": "lightgray"
}

app.layout = html.Div([
   html.H1("Supreme Court Decision Tracker"),
   dcc.Dropdown(
      id='decision-dropdown',
      options=[{'label': k, 'value': k} for k in SupremeCourtCheckData.SupremeCourtCheckData.keys()],
      value=list(SupremeCourtCheckData.SupremeCourtCheckData.keys())[0]
   ),
   dcc.Graph(id='state-choropleth')
])

@app.callback(
   Output('state-choropleth', 'figure'),
   Input('decision-dropdown', 'value')
)
def update_graph(selected_decision):
   policies = SupremeCourtCheckData.SupremeCourtCheckData[selected_decision]
    
   state_list = []
   policy_list = []
    
   for policy, states in policies.items():
      for state in states:
         state_list.append(state)
         policy_list.append(policy)

   df = pd.DataFrame({"states": state_list, "value": policy_list})

   fig = px.choropleth(
      df,
      locations="states",
      locationmode="USA-states",
      color="value",
      scope="usa",
      color_discrete_map=COLOR_MAP,
   )
    
   fig.update_layout(title=selected_decision, transition_duration=500)
   return fig

if __name__ == '__main__':
   app.run(debug=True)
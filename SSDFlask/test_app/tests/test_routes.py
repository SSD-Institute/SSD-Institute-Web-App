def test_homepage_status(client):
   response = client.get('/')
   assert response.status_code == 200

def test_plotly_in_html(client):
   response = client.get('/')
   assert b'id="results-bar-chart"' in response.data
   assert b'Plotly' in response.data
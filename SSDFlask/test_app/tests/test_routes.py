def test_homepage_status(client):
   response = client.get('/')
   assert response.status_code == 200

def test_collab_veto_status(client):
   response = client.get('/collaborative-veto')
   assert b'The Collaborative Veto tackles the often neglected'
   assert response.status_code == 200

def test_supreme_court_check_status(client):
   response = client.get('/supreme-court-check')
   assert b'When the Supreme Court issues a ruling'
   assert response.status_code == 200

def test_mcv_status(client):
   response = client.get('/multiple-choice-voting')
   assert b'The candidate with the most votes wins'
   assert response.status_code == 200

def test_minimum_space_status(client):
   response = client.get('/minimum-space')
   assert b'Minimum Amount of Space guarantees every'
   assert response.status_code == 200

def test_homepage_status(client):
   response = client.get('/contact')
   assert b'The Scientific Self-Determination project is'
   assert response.status_code == 200

def test_plotly_in_html(client):
   response = client.get('/')
   assert b'id="results-bar-chart"' in response.data
   assert b'Plotly' in response.data


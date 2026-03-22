import pytest
from app import app

def test_001_map_renders(dash_duo):
   dash_duo.start_server(app)

   dash_duo.wait_for_element("#state-choropleth", timeout=10)

   assert dash_duo.find_element("#state-choropleth").is_displayed()

   dash_duo.percy_snapshot("initial_map_load")

def test_002_dropdown_functional(dash_duo):
   dash_duo.start_server(app)

   dropdown = dash_duo.find_element("#decision-dropdown")
   dropdown.click()

   assert dash_duo.get_logs() == [], "Browser console should be clean."
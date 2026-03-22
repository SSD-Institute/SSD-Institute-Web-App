import pytest
from app import app

def test_001_map_renders(dash_duo):
   dash_duo.start_server(app)

   dash_duo.wait_for_element("#state-choropleth", timeout=10)

   assert dash_duo.find_element("#state-choropleth").is_displayed()

def test_002_dropdown_functional(dash_duo):
   dash_duo.start_server(app)

   dash_duo.wait_for_element("#decision-dropdown", timeout=10)

   dropdown = dash_duo.find_element("#decision-dropdown")
   assert dropdown.is_displayed()

   logs = dash_duo.get_logs()
   assert logs == [], f"Browser console errors found: {logs}"
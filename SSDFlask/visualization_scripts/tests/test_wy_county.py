import pytest
from wy_county_app import app

def test_001_wy_county_map_renders(dash_duo):
   dash_duo.start_server(app)

   dash_duo.wait_for_element("#wy-county-choropleth", timeout=15)

def test_002_wy_county_dropdown_functional(dash_duo):
   dash_duo.start_server(app)

   dash_duo.wait_for_element("#wy-county-dropdown", timeout=10)

   dropdown = dash_duo.find_element("#wy-county-dropdown")
   assert dropdown.is_displayed()

   logs = dash_duo.get_logs()
   assert logs == [], f"Browser console errors found: {logs}"

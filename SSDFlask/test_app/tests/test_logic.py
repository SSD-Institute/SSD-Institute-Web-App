import pytest
import pandas as pd
from utils.data_utils import filter_data_by_year, get_winner
from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

@pytest.fixture
def mock_df():
   return pd.DataFrame({
      'Year': ['1824', '1824'],
      'Candidate': ['Jackson', 'Adams'],
      'Method': ['Actual Results', 'Actual Results'],
      'Votes': [151271, 113122]
   })

def test_filter_year(mock_df):
   assert len(filter_data_by_year(mock_df, '1824')) == 2

def test_winner_calculation(mock_df):
   assert get_winner(mock_df, '1824') == 'Jackson'

def test_missing_file(mocker):
   mocker.patch("os.path.exists", return_value=False)
   from utils.data_utils import load_election_data
   with pytest.raises(FileNotFoundError):
      load_election_data("wrong.csv")

def test_update_chart_callback():
   from app import update_chart
   def run_cb():
      context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": "year-selector.value"}]}))
      return update_chart('1824')
   ctx = copy_context()
   _, msg = ctx.run(run_cb)
   assert "year-selector" in msg

def test_no_selection():
   from app import update_chart
   _, msg = update_chart(None)
   assert msg == "Select a year"
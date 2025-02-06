from dash import callback, ctx, dcc, Input, Output, State
import logging
from src.util.fetchers import fetch_synthetic_data

logging.basicConfig(level=logging.DEBUG)

# store fetched data
synthetic_data_store = dcc.Store(id='synthetic-data-store', data={})  

@callback(
  Output('synthetic-data-store', 'data'),
  Input('generate-button', 'n_clicks'),
  Input('start-over-button', 'n_clicks'),
  State('selected-dataset', 'data'),
  State('selected-count', 'data'),
  prevent_initial_call=True,
)
def fetch_or_reset_data(generate_clicks, reset_clicks, dataset, count):
  triggered_id = ctx.triggered_id  

  # reset synthetic data store
  if triggered_id == 'start-over-button':
    return {}

  # fetch new data
  if triggered_id == 'generate-button':
    if not dataset or not count:
      logging.error('Dataset or count is missing')
      return {}

    try:
      return fetch_synthetic_data(dataset, count)  # Fetch new data
    except Exception as e:
      logging.error(f'Error fetching synthetic data: {str(e)}')
      return {'data': [], 'diagnostics': None}

  # default case; should never be hit
  return {}

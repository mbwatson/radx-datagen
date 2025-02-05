from dash import callback, ctx, dcc, Input, Output, State
import dash_mantine_components as dmc
from src.components.generator.fetchers import fetch_synthetic_data
from dash_iconify import DashIconify
import json
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

generate_button = dmc.Button(
  'Generate',
  leftSection=DashIconify(icon='feather:cpu'),
  id='generate-button',
  n_clicks=0,
  variant='light',
  fullWidth=True,
  disabled=True,
)

# Toggle button visibility
@callback(
  Output('generate-button', 'disabled'),
  Input('dataset-select', 'value'),
  Input('count-select', 'value'),
)
def toggle_button_visibility(dataset, count):
  # Ensure both dataset and count are provided to enable the button
  return dataset is None or count is None

# Fetch synthetic data when the button is clicked
@callback(
  Output('synthetic-data-table', 'rowData'),
  Output('diagnostics-store', 'data'),
  Input('generate-button', 'n_clicks'),
  State('selected-dataset', 'data'),
  State('selected-count', 'data'),
  prevent_initial_call=True,
)
def fetch_data(n_clicks, dataset, count):
  # bail out if we're not here because the button was clicked
  if ctx.triggered_id != 'generate-button':
    return dash.no_update, dash.no_update

  # validate inputs
  if not dataset or not count:
    logging.error('Dataset or count is missing')
    return [], None  # Early return on invalid data

  try:
    synthetic_data = fetch_synthetic_data(dataset, count)

    data = synthetic_data['data']
    diagnostics = synthetic_data['diagnostics']

    # validate response format for AG Grid
    if isinstance(data, list) and all(isinstance(row, dict) for row in data):
      return data, diagnostics

    logging.error('Unexpected data format received')
    return [{'error': 'Unexpected data format received from API'}], diagnostics

  except Exception as e:
    logging.error(f'Error fetching synthetic data: {str(e)}')
    return [{'error': str(e)}], None  # Return error if any issue occurs

# update column definitions
@callback(
  Output('synthetic-data-table', 'columnDefs'),
  Input('generate-button', 'n_clicks'),
  Input('synthetic-data-table', 'rowData'),
  prevent_initial_call=True,
)
def update_columns(n_clicks, row_data):
  # If no data is present, return an empty list for columnDefs
  if not row_data:
    return []
  return [{'field': key} for key in row_data[0].keys()]

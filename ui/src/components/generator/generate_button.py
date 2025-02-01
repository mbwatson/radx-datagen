from dash import callback, ctx, dcc, Input, Output, State
import dash_mantine_components as dmc
from src.components.generator.fetchers import fetch_synthetic_data
from dash_iconify import DashIconify
import json

generate_button = dmc.Button(
  "Generate",
  leftSection=DashIconify(icon="feather:cpu"),
  id='generate-button',
  n_clicks=0,
  variant='light',
  fullWidth=True,
  disabled=True,
)

# toggle button visibility
@callback(
  Output('generate-button', 'disabled'),
  Input('dataset-select', 'value'),
  Input('count-select', 'value'),
)
def toggle_button_visibility(dataset, count):
  if dataset is not None and count is not None:
    return False
  return True

# fetch synthetic data, only when generate-button is clicked
@callback(
  Output('synthetic-data-table', 'rowData'),
  Input('generate-button', 'n_clicks'),
  State('selected-dataset', 'data'),
  State('selected-count', 'data'),
  prevent_initial_call=True,
)
def fetch_data(n_clicks, dataset, count):
  if ctx.triggered_id != 'generate-button':
    return dash.no_update

  if not dataset or not count:
    return []

  try:
    data = fetch_synthetic_data(dataset, count)
    
    # validate response format for AG Grid
    if isinstance(data, list) and all(isinstance(row, dict) for row in data):
      return data

    return [{"error": "Unexpected data format received from API"}]

  except Exception as e:
    return [{"error": str(e)}]  # Return error in a format AG Grid can display

@callback(
  Output('synthetic-data-table', 'columnDefs'),
  Input('generate-button', 'n_clicks'),
  Input('synthetic-data-table', 'rowData'),
  prevent_initial_call=True,
)
def update_columns(n_clicks, row_data):
  if not row_data:
    return []
  
  # define columns dynamically
  columns = [{"field": key} for key in row_data[0].keys()]
  return columns

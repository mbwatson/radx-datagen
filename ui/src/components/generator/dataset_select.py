from dash import Output, Input, html, callback
import dash_mantine_components as dmc
import requests
from src.components.generator.fetchers import fetch_datasets

dataset_select = html.Div([
  dmc.Select(
    label='Collection',
    placeholder='None selected',
    id='dataset-select',
    value='',
    data=[],
    mb=10,
  ),
])

# populate select options
@callback(
  Output('dataset-select', 'data'),
  Input('dataset-select', 'id'),
)
def update_select_options(_):
  available_datasets = fetch_datasets()
  return [{'label': item['name'], 'value': item['name']} for item in available_datasets]

# store selected dataset
@callback(
  Output('selected-dataset', 'data'),
  Input('dataset-select', 'value'),
)
def select_dataset(value):
  return f'{value}'

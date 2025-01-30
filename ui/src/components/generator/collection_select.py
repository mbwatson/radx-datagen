from dash import Output, Input, html, callback
import dash_mantine_components as dmc
import requests
from src.components.generator.fetchers import fetch_cde_collections

collection_select = html.Div([
  dmc.Select(
    label='Collection',
    placeholder='None selected',
    id='collection-select',
    value='',
    data=[],
    mb=10,
  ),
])

@callback(
  Output('collection-select', 'data'),
  Input('collection-select', 'id'),  # Triggered on component load
)
def update_select_options(_):
  available_collections = fetch_cde_collections()
  return [{'label': item['key'], 'value': item['key']} for item in available_collections]

@callback(
  Output('selected-collection', 'data'),
  Input('collection-select', 'value'),
)
def select_value(value):
  return f'{value}'
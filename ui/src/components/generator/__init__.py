from dash import callback, dcc, html, Input, Output
import dash_mantine_components as dmc
import json
import pandas
import requests
from src.components.generator.collection_select import collection_select
from src.components.generator.cde_select import cde_select

generator_form = dmc.Container(
  [
    dmc.Fieldset(
      legend='CDE Selection',
      children=[
        collection_select,
        cde_select,
      ],
      variant='transparent',
    ),
    dcc.Store(id='selected-collection'),
    dcc.Store(id='available-cdes'),
    dcc.Store(id='selected-cdes'),
  ],
  fluid=True,
  style={'margin': '1rem 0 0 0'},
)

# update selection summary
@callback(
  Output('form-selections', 'children'),
  Input('selected-collection', 'data'),
  Input('selected-cdes', 'data'),
)
def update_selections(collection, cde):
  return json.dumps({
    'collection': collection,
    'cdes': cde or [],
  }, indent=2)

from dash import callback, dcc, html, Input, Output
import dash_mantine_components as dmc
import json
from src.components.generator.fetchers import fetch_cdes_from_collection

cde_select = dmc.Fieldset(
  legend='CDEs',
  children=[
    dmc.ScrollArea(
      children=dcc.Checklist(
        id='cde-select',
        options=[],
        value=[],
        labelStyle={'display': 'flex', 'gap': '0.25rem'},
      ),
      h=500,
      w=350,
    ),
  ],
  style={'overflow-x': 'hidden'},
)

def cde_option(cde):
  return {
    'label': dmc.Group([
      cde['ids'][0]['id'],
      dmc.Code(cde['valueDomain']['datatype']),
    ]),
    'value': cde['ids'][0]['id'],
  }

# update select value
@callback(
  Output('cde-select', 'value'),
  Input('selected-collection', 'data'),
  prevent_initial_call=True
)
def update_select_value(_):
  return []

# update select options
@callback(
  Output('cde-select', 'options'),
  Input('selected-collection', 'data'),
  prevent_initial_call=True
)
def update_select_options(selected_collection):
  if not selected_collection:
    return []
  available_cdes = fetch_cdes_from_collection(selected_collection)
  return [cde_option(cde) for cde in available_cdes]

# store selections
@callback(
  Output('selected-cdes', 'data'),
  Input('cde-select', 'value'),
)
def select_value(value):
  return value

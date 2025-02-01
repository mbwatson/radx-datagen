from dash import callback, dcc, html, Input, Output
import dash_mantine_components as dmc
import json
import pandas
import requests
from .dataset_select import dataset_select
from .form_selections import form_selections
from .count_select import count_select
from .generate_button import generate_button
from .generated_data import generated_data

generator_form = dmc.Container(
  [
    dmc.Fieldset(
      legend='Generation Parameters',
      children=[
        dataset_select,
        count_select,
        generate_button,
      ],
      variant='transparent',
    ),
    dcc.Store(id='available-datasets'),
    dcc.Store(id='selected-dataset'),
    dcc.Store(id='selected-count'),
  ],
  fluid=True,
  style={'margin': '1rem 0 0 0'},
)

# update selection summary
@callback(
  Output('state-summary', 'children'),
  Input('selected-dataset', 'data'),
  Input('selected-count', 'data'),
)
def update_selection_summary(dataset, count):
  return json.dumps({
    'dataset': dataset or [],
    'count': count or '0',
  }, indent=2)

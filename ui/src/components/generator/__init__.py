from dash import callback, dcc, html, Input, Output
import dash_mantine_components as dmc

from .dataset_select import dataset_select
from .count_select import count_select
from .download_button import download_button
from .generate_button import generate_button
from .start_over_button import start_over_button
from .synthetic_data_store import synthetic_data_store

horizontal_rule = html.Div(style={
  'borderTop': '0.5px solid var(--mantine-color-default-border)',
  'marginTop': '1rem',
  'height': '1rem',
})

data_action_buttons = html.Div([
  horizontal_rule,
  dmc.Group(
    [
      download_button,
      start_over_button,
    ],
    grow=True,
  )],
  id='action-buttons',
)

generator_form = dmc.Container(
  [
    dmc.Fieldset(
      legend='Generation Parameters',
      children=[
        dataset_select,
        count_select,
        horizontal_rule,
        generate_button,
        data_action_buttons,
      ],
      variant='transparent',
      style={
        'margin': 'var(--mantine-spacing-md) 0 0 0',
        'width': '100%',
        'border': '1px solid var(--mantine-color-default-border)',
      },
    ),
    dcc.Store(id='selected-dataset'),
    dcc.Store(id='selected-count'),
    synthetic_data_store,
  ],
  fluid=True,
  style={ 'width': '100%' },
)

# toggle button visibility
@callback(
  Output('action-buttons', 'style'),
  Input('synthetic-data-table', 'rowData'),
)
def toggle_button_visibility(data):
  if data is None or len(data) == 0:
    return {'display': 'none'}
  return {'display': 'block'}

from .data_table import data_table
from .diagnostics_report import diagnostics_report
from .form_selections import form_selections

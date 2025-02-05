from dash import callback, dcc, html, Input, Output
import dash_mantine_components as dmc

from .dataset_select import dataset_select
from .count_select import count_select
from .download_button import download_button
from .generate_button import generate_button

horizontal_rule = html.Div(style={
  'borderTop': '0.5px solid var(--mantine-color-default-border)',
  'marginTop': '1rem',
  'height': '1rem',
})

generator_form = dmc.Container(
  [
    dmc.Fieldset(
      legend='Generation Parameters',
      children=[
        dataset_select,
        count_select,
        horizontal_rule,
        dmc.Group([generate_button, download_button]),
      ],
      variant='transparent',
      style={
        'margin': 'var(--mantine-spacing-sm) 0 0 0',
        'width': '100%',
        'border': '1px solid var(--mantine-color-default-border)',
      },
    ),
    dcc.Store(id='available-datasets'),
    dcc.Store(id='selected-dataset'),
    dcc.Store(id='selected-count'),
    dcc.Store(id='diagnostics-store'),
  ],
  fluid=True,
  style={ 'width': '100%' },
)

from .data_table import data_table
from .diagnostics_report import diagnostics_report
from .form_selections import form_selections

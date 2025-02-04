from dash import callback, dcc, html, Input, Output
import dash_mantine_components as dmc

from .dataset_select import dataset_select
from .count_select import count_select
from .generate_button import generate_button

horizontal_rule = html.Div(style={
  'border-top': '0.5px solid var(--mantine-color-default-border)',
  'margin-top': '1rem',
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
        generate_button,
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
  ],
  fluid=True,
  style={ 'width': '100%' },
)

from .form_selections import form_selections
from .generated_data import generated_data

from dash import callback, Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import logging

# set up logging
logging.basicConfig(level=logging.DEBUG)

generate_button = dmc.Button(
  'Generate',
  leftSection=DashIconify(icon='mingcute:ai-line'),
  id='generate-button',
  n_clicks=0,
  variant='light',
  fullWidth=True,
  disabled=True,
  style={'flex': '1'},
)

# toggle button enabled or disabled
@callback(
  Output('generate-button', 'disabled'),
  Input('dataset-select', 'value'),
  Input('count-select', 'value'),
)
def toggle_button_enabled_state(dataset, count):
  # ensure both dataset and count are provided to enable the button
  return dataset is None or count is None

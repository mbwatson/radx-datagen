import os
from dash import _dash_renderer, callback, Dash, dcc, html, Input, Output, State
import dash_mantine_components as dmc
from src.theme import DEFAULT_THEME
from src.components.header import header
from src.components.generator import data_table
from src.components.generator import diagnostics_report
from src.components.generator import generator_form
from src.components.generator import form_selections
import json

_dash_renderer._set_react_version('18.2.0')

app = Dash(__name__)
app.title = 'RADx Synthetic Data Dashboard'
app.layout = dmc.MantineProvider(
  theme=DEFAULT_THEME,
  id='mantine-provider',
  children=dmc.AppShell(
    [
      dmc.AppShellHeader(header),
      dmc.AppShellNavbar([
        generator_form,
        form_selections,
        diagnostics_report,
      ]),
      dmc.AppShellMain(
        dcc.Loading(
          id='loading',
          type='circle',
          children=[data_table]
        ),
      ),
    ],
    padding='md',
    id='app_shell',
    header={'height': 48},
    navbar={'width': 275}
  ),
)

server = app.server

if __name__ == '__main__':
  app.run_server(debug=True, host='0.0.0.0', port=os.getenv('UI_PORT'))

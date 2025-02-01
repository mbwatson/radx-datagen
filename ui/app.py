import os
from dash import _dash_renderer, callback, Dash, dcc, html, Input, Output, State
import dash_mantine_components as dmc
from src.theme import DEFAULT_THEME
from src.components.header import header
from src.components.generator import generator_form
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
      dmc.AppShellNavbar(generator_form),
      dmc.AppShellMain([
        html.Div('Selections:'),
        dmc.Code(id='form-selections', style={'whiteSpace': 'pre-wrap'})
      ]),
    ],
    padding='md',
    id='app_shell',
    header={'height': 48},
    navbar={'width': 400}
  ),
)

server = app.server

if __name__ == '__main__':
  app.run_server(debug=True)

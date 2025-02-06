import os
from dash import _dash_renderer, Dash, dcc
import dash_mantine_components as dmc
from src.theme import DEFAULT_THEME
from src.components.generator import data_table
from src.components.navbar import navbar

_dash_renderer._set_react_version('18.2.0')

app = Dash(__name__)
app.title = 'RADx Synthetic Data Generator'
app.layout = dmc.MantineProvider(
  theme=DEFAULT_THEME,
  id='mantine-provider',
  children=dmc.AppShell(
    [
      navbar,
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
    navbar={'width': 275}
  ),
)

server = app.server

if __name__ == '__main__':
  app.run_server(debug=True, host='0.0.0.0', port=os.getenv('UI_PORT'))

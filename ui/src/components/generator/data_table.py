from dash import callback, html, Input, Output
import dash_mantine_components as dmc
import dash_ag_grid as dag
from dash_iconify import DashIconify
from datetime import datetime
from .download_button import download_button

data_grid_toolbar = dmc.Paper(
  dmc.Group(
    grow=True,
    wrap="nowrap",
    children=[download_button],
  ),
  style={
    'display': 'flex',
    'justifyContent': 'flex-end',
    'margin': 'calc(var(--mantine-spacing-sm) / 2) 0 var(--mantine-spacing-sm) 0',
    'padding': '4px'
  },
  withBorder=True,
)

data_grid = dag.AgGrid(
  id='synthetic-data-table',
  columnDefs=[{'field': 'key'}, {'field': 'value'}],
  rowData=[],
  dashGridOptions={'domLayout': 'normal'},
  style={
    'height': 'calc(100vh - var(--app-shell-header-height) - 2*var(--mantine-spacing-md) - 4rem)',
    'width': '100%',
  },
  csvExportParams={'fileName': 'radx-datagen.csv'},
)


data_table = html.Div([
  data_grid_toolbar,
  data_grid,
])

# data table light and dark theme classes
grid_class = {
  'light': 'ag-theme-balham',
  'dark': 'ag-theme-balham-dark',
}

# align chart and table styles with current color scheme setting
@callback(
  Output('synthetic-data-table', 'className'),
  Input('theme-store', 'data'),
)
def align_chart_theme(theme):
  return grid_class[theme]

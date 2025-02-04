from dash import callback, html, Input, Output
import dash_mantine_components as dmc
import dash_ag_grid as dag
from dash_iconify import DashIconify
from datetime import datetime

download_button = dmc.Tooltip(
  label='Download as CSV',
  position='bottom-end',
  offset=3,
  withArrow=True,
  arrowSize=8,
  arrowOffset=21,
  transitionProps={
    'transition': 'slide-up', 
    'duration': 100,
    'timingFunction': 'ease'
  },
  children=dmc.Button(
    DashIconify(icon='feather:download-cloud'),
    id='download-button',
    variant='light',
    size='xs',
    n_clicks=0,
  )
)

data_grid_toolbar = dmc.Paper(
  dmc.Group(
    grow=True,
    wrap="nowrap",
    children=[download_button],
  ),
  style={
    'display': 'flex',
    'justify-content': 'flex-end',
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


generated_data = html.Div([
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

# export table data as csv on export button click
@callback(
  Output('synthetic-data-table', 'csvExportParams'),
  Output('synthetic-data-table', 'exportDataAsCsv'),
  Input('download-button', 'n_clicks'),
)
def export_data_as_csv(n_clicks):
  if n_clicks:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'radx-datagen_{timestamp}.csv'
    return {'fileName': filename}, True
  return {'fileName': 'radx-datagen.csv'}, False

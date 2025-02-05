from dash import callback, html, Input, Output
import dash_mantine_components as dmc
import dash_ag_grid as dag
from dash_iconify import DashIconify
from datetime import datetime
from .download_button import download_button

data_table = dag.AgGrid(
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

# data table light and dark theme classes
table_class = {
  'light': 'ag-theme-balham',
  'dark': 'ag-theme-balham-dark',
}

# align table style with current color scheme setting
@callback(
  Output('synthetic-data-table', 'className'),
  Input('theme-store', 'data'),
)
def align_table_theme(theme):
  return table_class[theme]

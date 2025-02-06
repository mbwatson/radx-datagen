from dash import callback, Input, Output
import dash_ag_grid as dag

data_table = dag.AgGrid(
  id='synthetic-data-table',
  columnDefs=[{'field': 'key'}, {'field': 'value'}],
  rowData=[],
  dashGridOptions={'domLayout': 'normal'},
  style={
    'marginTop': 'var(--mantine-spacing-xs)',
    'height': 'calc(100vh - var(--app-shell-header-height) - 2*var(--mantine-spacing-lg))',
    'width': '100%',
  },
  csvExportParams={'fileName': 'radx-datagen.csv'},
)

# data table light and dark theme classes
table_class = {
  'light': 'ag-theme-balham',
  'dark': 'ag-theme-balham-dark',
}

# update table from store
@callback(
  Output('synthetic-data-table', 'columnDefs'),
  Output('synthetic-data-table', 'rowData'),
  Input('synthetic-data-store', 'data'),
)
def update_table(synthetic_data_store):
  data = synthetic_data_store.get('data', [])
  if not data:
    return [], []
  return [{'field': key} for key in data[0].keys()], data

# align table style with current color scheme setting
@callback(
  Output('synthetic-data-table', 'className'),
  Input('theme-store', 'data'),
)
def align_table_theme(theme):
  return table_class[theme]

from dash import callback, html, Input, Output
import dash_ag_grid as dag

generated_data = dag.AgGrid(
  id='synthetic-data-table',
  columnDefs=[{"field": "key"}, {"field": "value"}],
  rowData=[],
  dashGridOptions={"domLayout": "normal"},
  style={
    "height": "calc(100vh - var(--app-shell-header-height) - 2*var(--mantine-spacing-md) - 10px)",
    "margin-top": "10px",
    "width": "100%",
  }
)

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
from dash import html
import dash_ag_grid as dag

generated_data = dag.AgGrid(
  id='synthetic-data-table',
  columnDefs=[{"field": "key"}, {"field": "value"}],
  rowData=[]
)

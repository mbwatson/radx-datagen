from dash import callback, Input, Output
import dash_mantine_components as dmc
import json

diagnostics_report = dmc.Code(
  id='diagnostics-report',
  style={
    'whiteSpace': 'pre-wrap',
    'margin': '0 var(--mantine-spacing-md)',
    'padding': 'var(--mantine-spacing-sm)',
    'border': '1px solid var(--mantine-color-default-border)',
    'fontSize': '60%',
  },
  block=True,
  variant='outlined',
)

# update report details on new data
@callback(
  Output('diagnostics-report', 'children'),
  Input('synthetic-data-store', 'data'),
)
def update_diagnostics(data_store):
  return 'DIAGNOSTICS = ' + json.dumps(data_store.get('diagnostics', None), indent=2)

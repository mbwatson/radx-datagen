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

# align table style with current color scheme setting
@callback(
  Output('diagnostics-report', 'children'),
  Input('diagnostics-store', 'data'),
)
def populate_diagnostics_report(data):
  return 'DIAGNOSTICS = ' + json.dumps(data, indent=2)

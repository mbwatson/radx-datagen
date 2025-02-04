from dash import callback, Input, Output
import dash_mantine_components as dmc
import json

form_selections = dmc.Code(
  id='state-summary',
  style={
    'whiteSpace': 'pre-wrap',
    'margin': 'var(--mantine-spacing-md)',
    'padding': 'var(--mantine-spacing-sm)',
    'border': '1px solid var(--mantine-color-default-border)',
    'font-size': '60%',
  },
  block=True,
  variant='outlined',
)

# update selection summary
@callback(
  Output('state-summary', 'children'),
  Input('selected-dataset', 'data'),
  Input('selected-count', 'data'),
)
def update_selection_summary(dataset, count):
  return json.dumps({
    'DATASET': dataset or [],
    'COUNT': count or '0',
  }, indent=2)

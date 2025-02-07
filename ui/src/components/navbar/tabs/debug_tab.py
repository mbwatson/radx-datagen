from dash import callback, Input, Output
import dash_mantine_components as dmc
import json
from src.components.theme_toggle import theme_toggle
from .tab_heading import tab_heading

debug_tab = dmc.Box([
  tab_heading('DEBUG'),
  dmc.Code(
    id='debug-json',
    style={
      'whiteSpace': 'pre-wrap',
      'padding': 'var(--mantine-spacing-sm)',
      'border': '1px solid var(--mantine-color-default-border)',
      'fontSize': '60%',
      'borderRadius': '0',
      'backgroundColor': 'transparent',
    },
    block=True,
    variant='outlined',
  ),
])

# update application state summary
@callback(
  Output('debug-json', 'children'),
  Input('selected-dataset', 'data'),
  Input('selected-count', 'data'),
  Input('synthetic-data-store', 'data'),
)
def update_contents(dataset, count, data_store):
  return json.dumps({
    'FORM_STATE': {
      'DATASET': dataset or [],
      'COUNT': count or '0',
    },
    'DIAGNOSTICS': data_store.get('diagnostics', None),
  }, indent=2)

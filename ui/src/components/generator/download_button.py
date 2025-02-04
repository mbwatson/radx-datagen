from dash import callback, html, Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from datetime import datetime

download_button = dmc.Tooltip(
  label='Download as CSV',
  position='top',
  offset=3,
  withArrow=True,
  arrowSize=8,
  arrowOffset=21,
  transitionProps={
    'transition': 'fade', 
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

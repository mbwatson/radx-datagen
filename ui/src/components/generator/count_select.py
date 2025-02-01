from dash import callback, dcc, html, Input, Output

import dash_mantine_components as dmc

count_select = html.Div(
  dmc.Select(
    label='Count',
    placeholder='None selected',
    id='count-select',
    value='',
    data=['1', '5', '10'],
    mb=10,
  )
)

# store selected count
@callback(
  Output('selected-count', 'data'),
  Input('count-select', 'value'),
)
def select_count_value(value):
  return f'{value}'


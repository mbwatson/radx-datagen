from dash import callback, dcc, html, Input, Output

import dash_mantine_components as dmc

count_select = html.Div(
  dmc.Select(
    label='COUNT',
    placeholder='None selected',
    checkIconPosition="right",
    id='count-select',
    value='5',
    data=['5', '10', '50', '100', '1000'],
    required=True,
    mb=10,
    variant='filled',
    labelProps={'style': {'fontSize': '75%'} }
  )
)

# store selected count
@callback(
  Output('selected-count', 'data'),
  Input('count-select', 'value'),
)
def select_count_value(value):
  return f'{value}'


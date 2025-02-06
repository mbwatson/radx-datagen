from dash import callback, html, Output, Input
import dash_mantine_components as dmc

from src.util.fetchers import fetch_datasets

dataset_select = html.Div([
    dmc.Select(
        label='DATASET',
        placeholder='None selected',
        checkIconPosition='right',
        id='dataset-select',
        value='',
        data=[],
        required=True,
        variant='filled',
        mb=10,
        labelProps={'style': {'fontSize': '75%'}},
        comboboxProps={'transitionProps': {'transition': 'pop'}},
    ),
])

@callback(
    Output('dataset-select', 'data'),
    Input('dataset-select', 'id'),
)
def update_select_options(_):
    """Update select options with available datasets."""
    available_datasets = fetch_datasets()
    return [{'group': key, 'items': value} for key, value in available_datasets.items()]


# store selected dataset
@callback(
    Output('selected-dataset', 'data'),
    Input('dataset-select', 'value'),
)
def select_dataset(value):
    return f'{value}'

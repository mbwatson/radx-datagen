import dash_mantine_components as dmc
from src.components.github_link import github_link
from .tab_heading import tab_heading

info_tab = dmc.Box([
    tab_heading('INFO'),
    dmc.Box([
        github_link,
    ], style={'padding': '1rem'}),
])

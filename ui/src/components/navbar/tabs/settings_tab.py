import dash_mantine_components as dmc
from src.components.theme_toggle import theme_toggle
from .tab_heading import tab_heading

settings_tab = dmc.Box([
    tab_heading('SETTINGS'),
    dmc.Box([
        theme_toggle,
    ], style={'padding': '1rem'}),
])

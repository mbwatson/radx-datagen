from dash import html, dcc, callback, Input, Output, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify

import dash_mantine_components as dmc
from dash_iconify import DashIconify

from .tabs import settings_tab, info_tab, debug_tab

footer_tabs = dmc.Tabs(
    [
        dmc.TabsPanel(settings_tab, value='settings'),
        dmc.TabsPanel(info_tab, value='info'),
        dmc.TabsPanel(debug_tab, value='debug'),
        dmc.TabsList(
            [
                dmc.TabsTab(DashIconify(icon='mingcute:settings-2-line'), value='settings'),
                dmc.TabsTab(DashIconify(icon='mingcute:information-line'), value='info'),
                dmc.TabsTab(DashIconify(icon='mingcute:bug-line'), value='debug'),
            ],
            grow=True
        ),
    ],
    id='footer-tabs',
    value=None,
    allowTabDeactivation=True,
    classNames={'tab': 'footer-tabs'},
)

navbar_footer = dmc.Paper(
    children=[
        footer_tabs,
        dcc.Store(id='active_tab_store', data=None),
    ],
    style={
        'borderRadius': 0,
        'borderTop': '1px solid var(--mantine-color-default-border)',
        'backgroundColor': 'color-mix(in srgb, var(--mantine-color-body), var(--mantine-primary-color-8) 10%)',
    },
)

@callback(
    Output('footer-tabs', 'value'),
    Output('active_tab_store', 'data'),
    Input('footer-tabs', 'value'),
    State('active_tab_store', 'data'),
    prevent_initial_call=True,
)
def toggle_tab(clicked_tab, current_tab):
    if clicked_tab == current_tab:
        return None, None
    return clicked_tab, clicked_tab

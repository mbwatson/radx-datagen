import dash_mantine_components as dmc
from dash_iconify import DashIconify
from .theme_toggle import theme_toggle
from .github_link import github_link

navbar_footer = dmc.Paper(
  children=[
    dmc.Group([theme_toggle, github_link]),
  ],
  style={
    'borderRadius': 0,
    'padding': 'var(--mantine-spacing-xs)',
    'borderTop': '1px solid var(--mantine-color-default-border)',
    'backgroundColor': 'color-mix(in srgb, var(--mantine-color-body), var(--mantine-primary-color-8) 10%)',
  },
)

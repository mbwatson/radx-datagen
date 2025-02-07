import dash_mantine_components as dmc
from dash_iconify import DashIconify

github_link = dmc.Anchor(
  DashIconify(icon='mingcute:github-line', width=20, color='var(--mantine-color-text)'),
  variant='transparent',
  id='github-link',
  href='https://github.com/mbwatson/radx-datagen',
  target='_blank',
  style={'display': 'flex', 'padding': '7px'},
)

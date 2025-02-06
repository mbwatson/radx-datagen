from dash import callback, dcc, Input, Output, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from src.components.theme_toggle import theme_toggle

app_logo = dmc.Anchor("RADx Synthetic Data Generator", href="/")

github_link = dmc.Anchor(
  DashIconify(icon="mingcute:github-line", width=20, color="var(--mantine-color-text)"),
  variant="transparent",
  id="github-link",
  href="https://github.com/mbwatson/radx-datagen",
  target="_blank",
  style={'display': 'flex'},
)

header = dmc.Flex(
  children=[
    app_logo,
    dmc.Group(
      [github_link, theme_toggle],
      style={'alignItems': 'center'}
    ),
  ],
  justify="space-between",
  align="center",
  style={"flex": 1},
  h="100%",
  px="md",
)

from dash import callback, html, Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from datetime import datetime

start_over_button = dmc.Button(
  DashIconify(icon='feather:rotate-ccw'),
  id='start-over-button',
  variant='light',
  n_clicks=0,
)

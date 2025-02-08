from dash import callback, Input, Output
import dash_mantine_components as dmc
from src.components.theme_toggle import theme_toggle
import json

def tab_heading(title):
  return dmc.Text(
    title,
    size='xs',
    style={
      'textAlign': 'center',
      'padding': '4px var(--mantine-spacing-md)',
      'backgroundColor': 'var(--mantine-primary-color-light-hover)',
    }
  )

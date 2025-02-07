from dash import callback, Input, Output
import dash_mantine_components as dmc
from src.components.theme_toggle import theme_toggle
import json

def tab_heading(title):
  return dmc.Text(
    title,
    size='xs',
    style={
      'backgroundColor': 'var(--mantine-primary-color-light-hover)',
      'padding': 'var(--mantine-spacing-xs)',
    }
  )

from dash import callback, dcc, Input, Output, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify

nav_items = [
  {"label": "Home", "href": "/"},
]

def nav_link(label, href):
  return dmc.NavLink(
    label=label,
    href=href,
    variant="subtle",
  )

nav_links = [nav_link(label=item["label"], href=item["href"]) for item in nav_items]

menu = dmc.Stack(nav_links, gap="0")

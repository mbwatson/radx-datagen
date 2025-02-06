import dash_mantine_components as dmc

from .header import navbar_header
from .footer import navbar_footer

from src.components.generator import diagnostics_report
from src.components.generator import form_selections
from src.components.generator import generator_form

navbar = dmc.AppShellNavbar(
  dmc.Stack(
    [
      dmc.Stack(
        [
          navbar_header, 
          generator_form,
        ],
        gap='xs',
      ),
      dmc.Stack(
        [
          diagnostics_report, 
          form_selections, 
          navbar_footer,
        ],
        gap='xs'
      ),
    ],
    justify='space-between',
    style={
      'height': '100vh',
    },
  )
)

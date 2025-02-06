import dash_mantine_components as dmc

navbar_header = dmc.Paper(
  dmc.Text('RADx Synthetic Data Generator'),
  style={
    'borderRadius': 0,
    'padding': 'var(--mantine-spacing-xs)',
    'borderBottom': '1px solid var(--mantine-color-default-border)',
    'backgroundColor': 'color-mix(in srgb, var(--mantine-color-body), var(--mantine-primary-color-8) 10%)',
    'textAlign': 'center',
  },
)

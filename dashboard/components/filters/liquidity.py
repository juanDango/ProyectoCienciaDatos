from dash import dcc

def liquidity_filter():
    return dcc.Slider(
        id='liquidity-filter',
        min=0,
        max=10,
        step=0.1,
        marks={i: f'{i}' for i in range(0, 11)},
        value=1
    )
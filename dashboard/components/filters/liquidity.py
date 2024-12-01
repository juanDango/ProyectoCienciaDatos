from dash import dcc


def liquidity_filter():
    return dcc.RangeSlider(
        id='liquidity-filter',
        min=0,
        max=4000,
        step=100,
        marks={i: f'{i}' for i in range(0, 4001, 1000)},
        value=[0, 4001]
    )
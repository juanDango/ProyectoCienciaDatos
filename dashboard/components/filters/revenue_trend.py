from dash import dcc


def revenue_trend_filter():
    return dcc.RangeSlider(
        id='revenue-trend-filter',
        min=-300000,
        max=50000,
        step=1,
        marks={i: f'{i}' for i in range(-300000, 50001, 70000)},
        value=[-300000, 50000]
    )
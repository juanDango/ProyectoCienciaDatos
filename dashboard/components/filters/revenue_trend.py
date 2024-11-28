from dash import dcc

def revenue_trend_filter():
    return dcc.RangeSlider(
        id='revenue-trend-filter',
        min=-100,
        max=100,
        step=1,
        marks={i: f'{i}%' for i in range(-100, 101, 20)},
        value=[-10, 10]
    )
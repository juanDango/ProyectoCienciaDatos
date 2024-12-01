from dash import dcc


def total_revenue_filter():
    return dcc.RangeSlider(
        id='total-revenue-filter',
        min=-8e3,
        max=2e8,
        step=1e6,
        marks={i: f'{int(i/1e6)}M' for i in range(int(-8e3), int(2e8)+1, int(4e7))},
        value=[-8e3, 2e8]
    )

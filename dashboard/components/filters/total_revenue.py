from dash import dcc

def total_revenue_filter():
    return dcc.RangeSlider(
        id='total-revenue-filter',
        min=0,
        max=1.5e8,
        step=1e6,
        marks={i: f'{int(i/1e6)}M' for i in range(0, int(1.5e8)+1, int(2e7))},
        value=[0, 1e7]
    )

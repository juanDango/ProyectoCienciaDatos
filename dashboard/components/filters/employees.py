from dash import dcc

def employees_filter():
    return dcc.RangeSlider(
        id='employees-filter',
        min=0,
        max=50000,
        step=1000,
        marks={i: f'{i}' for i in range(0, 50001, 10000)},
        value=[0, 5000]
    )
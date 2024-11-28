from dash import dcc

def long_term_debt_filter():
    return dcc.RangeSlider(
        id='long-term-debt-filter',
        min=0,
        max=1e8,
        step=1e6,
        marks={i: f'{int(i/1e6)}M' for i in range(0, int(1e8)+1, int(1e7))},
        value=[0, 1e7]
    )

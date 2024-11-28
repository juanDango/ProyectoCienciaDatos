from dash import dcc

def short_term_debt_filter():
    return dcc.RangeSlider(
        id='short-term-debt-filter',
        min=0,
        max=1e7,
        step=1e5,
        marks={i: f'{int(i/1e6)}M' for i in range(0, int(1e7)+1, int(1e6))},
        value=[0, 1e6]
    )

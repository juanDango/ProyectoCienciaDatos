from dash import dcc


def short_term_debt_filter():
    return dcc.RangeSlider(
        id='short-term-debt-filter',
        min=-1e7,
        max=1e7,
        step=1e5,
        marks={i: f'{int(i/1e6)}M' for i in range(int(-1e7), int(1e7)+1, 5000000 )},
        value=[-1e7, 1e7]
    )

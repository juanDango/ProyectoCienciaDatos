from dash import dcc


def industry_filter():
    return dcc.Dropdown(
        id='industry-filter',
        options=[],
        placeholder='Select Industry',
        multi=True
    )

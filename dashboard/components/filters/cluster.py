from dash import dcc


def cluster_filter():
    return dcc.Dropdown(
        id='cluster-filter',
        options=[],
        placeholder='Select Cluster',
        multi=True
    )
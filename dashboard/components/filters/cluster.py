from dash import dcc

def cluster_filter():
    return dcc.Dropdown(
        id='cluster-filter',
        options=[
            {'label': f'Cluster {i}', 'value': i} for i in range(1, 6)
        ],
        placeholder='Select Cluster',
        multi=True
    )
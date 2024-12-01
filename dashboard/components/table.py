from dash import dash_table


def result_table():
    return dash_table.DataTable(
        id='result-table',
        columns=[],
        data=[],
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'padding': '5px',
        },
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    )
from dash import dcc
from dash import html

def upload_component():
    return html.Div(
        [
            dcc.Upload(
                id='upload-data',
                children=html.Div(['Arrastra o selecciona un archivo Excel']),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                multiple=False
            ),
            html.Div(id='upload-status', style={'marginTop': '10px'})
        ]
    )

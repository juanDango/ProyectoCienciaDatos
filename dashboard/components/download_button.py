import dash_bootstrap_components as dbc
from dash import dcc, html


def download_button():
    return html.Div(
        [
            dbc.Button(
                "Descargar Resultados",
                id="download-results",
                color="success",
                className="me-2",
                n_clicks=0
            ),
            dcc.Download(id="download-dataframe-xlsx")
        ]
    )

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, ctx


dash.register_page(__name__, path="/segmentacion")


def upload_component():
    return dcc.Upload(
        id="upload-data",
        children=html.Div(["Arrastra o selecciona un archivo Excel aquí"]),
        style={
            "width": "100%",
            "height": "60px",
            "lineHeight": "60px",
            "borderWidth": "1px",
            "borderStyle": "dashed",
            "borderRadius": "5px",
            "textAlign": "center",
            "margin": "10px",
        },
        multiple=False,
    )

def process_button():
    return dbc.Button("Procesar", id="process-button", color="primary", className="w-100", disabled=True)

def download_button():
    return dbc.Button("Descargar", id="download-button", color="success", className="w-100", disabled=True)

def result_table():
    return html.Div(
        id="result-table-container",
        children=[],
    )

layout = dbc.Container(
    [
        html.H1("Clústeres con Modelo Entrenado", className="text-center mb-4"),
        dbc.Row(
            [
                dbc.Col(upload_component(), width=6),
                dbc.Col(process_button(), width=6),
            ],
            className="mb-3",
        ),
        dbc.Row(
            [
                dbc.Col(result_table(), width=12),
            ],
            className="mb-3",
        ),
        dbc.Row(
            [
                dbc.Col(download_button(), width=12),
            ],
            className="mb-3",
        ),
        dbc.Alert(
            id="upload-alert",
            children="",
            color="danger",
            dismissable=True,
            is_open=False,
            className="mt-3",
        ),
        dcc.Store(id="processed-data"),
        dcc.Download(id="download-dataframe-csv"),
    ],
    fluid=True,
)
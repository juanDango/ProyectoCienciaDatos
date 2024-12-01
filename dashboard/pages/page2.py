import dash
import dash_bootstrap_components as dbc
from dash import html

from components.download_button import download_button
from components.process_button import process_button
from components.table import result_table
from components.upload import upload_component

dash.register_page(__name__, path="/segmentacion")

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
    ],
    fluid=True
)
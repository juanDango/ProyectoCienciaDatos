import dash
import dash_bootstrap_components as dbc
from dash import html


dash.register_page(__name__, path="/")

layout = dbc.Container(
    [
        html.Div(
            className="content",
            children=[
                html.Div(
                    className="left_menu",
                    children=[
                        html.Div(
                            className="grid_left",
                            children=[
                                dbc.Row(
                                    "FILTROS",
                                    class_name="left_div div1_left",
                                ),
                                dbc.Row(
                                    children=[
                                    ],
                                    class_name="left_div div2_left",
                                ),
                                dbc.Row(
                                    children=[
                                    ],
                                    class_name="left_div div2_left",
                                ),
                                dbc.Row(
                                    children=[
                                    ],
                                    class_name="left_div div2_left",
                                ),
                                dbc.Row(
                                    children=[
                                    ],
                                    class_name="left_div div2_left",
                                ),
                                dbc.Row(
                                    children=[
                                    ],
                                    class_name="left_div div2_left",
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="right_content",
                    children=[
                        html.Div(
                            className="grid",
                            children=[
                                dbc.Row(
                                    className="right_div div1",
                                    children=[
                                    ],
                                ),
                                dbc.Row(
                                    class_name="right_div div2",
                                    children=[
                                    ],
                                ),
                                dbc.Row(
                                    class_name="right_div div3",
                                    children=[
                                    ],
                                ),
                                dbc.Row(
                                    className="right_div div4",
                                    children=[
                                    ],
                                ),
                                dbc.Row(
                                    class_name="right_div div5",
                                    children=[
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
            ],
        ),
    ],
    fluid=True,
    class_name="px-0",
)



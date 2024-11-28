import dash_bootstrap_components as dbc
from dash import html

LOGO = "https://data.org/wp-content/uploads/2022/02/Universidad-de-los-Andes.png"

links = dbc.Row(
    [
        dbc.Col(html.A("INICIO", href="/")),
        dbc.Col(html.A("NUEVO", href="/segmentacion")),
    ],
    align="center",
    className="g-6 ms-auto",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px", className="ms-4")),
                        dbc.Col(
                            dbc.NavbarBrand(
                                "PROYECTO CIENCIA DE DATOS", className="ms-2"
                            )
                        ),
                    ],
                ),
                href="https://www.uniandes.edu.co/",
                style={"textDecoration": "solid"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                links,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
        fluid=True,
        class_name="navbar",
    ),
    color="white",
    dark=False,
)

import dash
import dash_bootstrap_components as dbc
from dash import Dash

from components.navbar import navbar

app = Dash(
    __name__,
    use_pages=True,
    assets_folder="assets",
    pages_folder="pages",
    title="ProyectoCienciaDatos",
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.LITERA,
        dbc.icons.FONT_AWESOME,
        "assets/styles.css",
    ],
)


def create_layout():
    layout = dbc.Container(
        id="display",
        children=[
            navbar,
            dash.page_container,
        ],
        fluid=True,
        class_name="px-0",
    )
    return layout

app.layout = create_layout()


if __name__ == "__main__":
    app.run(debug=True)
    # app.run_server(host="0.0.0.0", port="8050") # For compose!!!

import dash_bootstrap_components as dbc


def process_button():
    return dbc.Button(
        "Calcular Clústeres",
        id="process-clusters",
        color="primary",
        className="me-2",
        n_clicks=0
    )
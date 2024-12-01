import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output

from components.navbar import navbar
from utils.data_loader import DataLoader
from components.charts.opportunities import OpportunitiesChart


app = Dash(
    __name__,
    use_pages=True,
    assets_folder="assets",
    pages_folder="pages",
    suppress_callback_exceptions=True,
    title="ProyectoCienciaDatos",
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

################## FILTERS ##################
### Cluster filter
@app.callback(
    Output('cluster-filter', 'options'),
    Input('data-loaded', 'data')
)
def test_callback(_):
    data = DataLoader(file_path="datos/complete_payload.json").get_data()
    available_clusters = data['cluster'].unique()
    options = [{'label': f'Cluster {i}', 'value': i} for i in sorted(available_clusters)]
    return options

################## CHARTS ##################
@app.callback(
    Output('opportunities-chart', 'children'),
    Input('cluster-filter', 'value')
)
def update_opportunities_chart(selected_clusters):
    full_data = DataLoader(file_path="datos/complete_payload.json")
    filtered_data = full_data.get_data().copy()
    if selected_clusters:
        filtered_data = filtered_data[filtered_data['cluster'].isin(selected_clusters)]
        print("Here!!!")
    else:
        filtered_data = filtered_data
    print(filtered_data.shape)
    return OpportunitiesChart(
        data=filtered_data,
        id_graph="opportunities-chart"
    ).render()


if __name__ == "__main__":
    app.run(debug=True)
    # app.run_server(host="0.0.0.0", port="8050") # For compose!!!

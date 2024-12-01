import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, html, State, dcc

from callbacks.calbback_industry_filter import industry_filter_callback_logic
from callbacks.callback_cluster_filter import cluster_filter_callback_logic
from callbacks.callback_debtreduction_chart import \
    update_debtreduction_chart_logic
from callbacks.callback_highdebt_chart import update_highdebt_chart_logic
from callbacks.callback_liquidity_chart import update_liquidity_chart_logic
from callbacks.callback_operational_capacity_chart import \
    update_operationalcapacity_chart_logic
from callbacks.callback_opportunities_chart import \
    update_opportunities_chart_logic
from callbacks.callback_revenue_chart import update_revenue_chart_logic
from callbacks.callback_roaroe_chart import update_roaroe_chart_logic
from callbacks.callback_sector_chart import update_sector_chart_logic
from components.navbar import navbar
from dash.dash_table import DataTable
import pandas as pd
import base64
from io import BytesIO
import requests


def consume_classifier_api(api_url, payload):
    """
    Consume el método classifier de una API.

    :param api_url: URL base de la API.
    :param payload: Datos que se enviarán en la solicitud POST (en formato JSON).
    :return: Respuesta de la API como un diccionario.
    """
    try:
        endpoint = f"{api_url}/classify"
        response = requests.post(endpoint, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error al consumir la API: {e}")
        return None


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

################## FILTERS ####################################
### Cluster filter
@app.callback(
    Output('cluster-filter', 'options'),
    Input('data-loaded', 'data')
)
def cluster_filter_callback(_):
    return cluster_filter_callback_logic()

### Industry filter
@app.callback(
    Output('industry-filter', 'options'),
    Input('data-loaded', 'data')
)
def industry_filter_callback(_):
    return industry_filter_callback_logic()

################## CHARTS ####################################
@app.callback(
    Output('opportunities', 'children'),
    [
        Input('cluster-filter', 'value'),
        Input('industry-filter', 'value'),
        Input('revenue-trend-filter', 'value'),
        Input('employees-filter', 'value'),
        Input('liquidity-filter', 'value'),
        Input('short-term-debt-filter', 'value'),
        Input('long-term-debt-filter', 'value'),
        Input('total-revenue-filter', 'value')
    ]
)
def update_opportunities_chart(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue):
    return update_opportunities_chart_logic(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue)

@app.callback(
    Output('roa_roe', 'children'),
    [
        Input('cluster-filter', 'value'),
        Input('industry-filter', 'value'),
        Input('revenue-trend-filter', 'value'),
        Input('employees-filter', 'value'),
        Input('liquidity-filter', 'value'),
        Input('short-term-debt-filter', 'value'),
        Input('long-term-debt-filter', 'value'),
        Input('total-revenue-filter', 'value')
    ]
)
def update_roaroe_chart(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue):
    return update_roaroe_chart_logic(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue)


@app.callback(
    Output('revenue', 'children'),
    [
        Input('cluster-filter', 'value'),
        Input('industry-filter', 'value'),
        Input('revenue-trend-filter', 'value'),
        Input('employees-filter', 'value'),
        Input('liquidity-filter', 'value'),
        Input('short-term-debt-filter', 'value'),
        Input('long-term-debt-filter', 'value'),
        Input('total-revenue-filter', 'value')
    ]
)
def update_revenue_chart(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue):
    return update_revenue_chart_logic(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue)

@app.callback(
    Output('quick', 'children'),
    [
        Input('cluster-filter', 'value'),
        Input('industry-filter', 'value'),
        Input('revenue-trend-filter', 'value'),
        Input('employees-filter', 'value'),
        Input('liquidity-filter', 'value'),
        Input('short-term-debt-filter', 'value'),
        Input('long-term-debt-filter', 'value'),
        Input('total-revenue-filter', 'value')
    ]
)
def update_liquidity_chart(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue):
    return update_liquidity_chart_logic(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue)

@app.callback(
    Output('highdebt', 'children'),
    [
        Input('cluster-filter', 'value'),
        Input('industry-filter', 'value'),
        Input('revenue-trend-filter', 'value'),
        Input('employees-filter', 'value'),
        Input('liquidity-filter', 'value'),
        Input('short-term-debt-filter', 'value'),
        Input('long-term-debt-filter', 'value'),
        Input('total-revenue-filter', 'value')
    ]
)
def update_highdebt_chart(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue):
    return update_highdebt_chart_logic(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue)

@app.callback(
    Output('o_revenue', 'children'),
    [
        Input('cluster-filter', 'value'),
        Input('industry-filter', 'value'),
        Input('revenue-trend-filter', 'value'),
        Input('employees-filter', 'value'),
        Input('liquidity-filter', 'value'),
        Input('short-term-debt-filter', 'value'),
        Input('long-term-debt-filter', 'value'),
        Input('total-revenue-filter', 'value')
    ]
)
def update_operationalcapacity_chart(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue):
    return update_operationalcapacity_chart_logic(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue)


@app.callback(
    Output('debt_reduction', 'children'),
    [
        Input('cluster-filter', 'value'),
        Input('industry-filter', 'value'),
        Input('revenue-trend-filter', 'value'),
        Input('employees-filter', 'value'),
        Input('liquidity-filter', 'value'),
        Input('short-term-debt-filter', 'value'),
        Input('long-term-debt-filter', 'value'),
        Input('total-revenue-filter', 'value')
    ]
)
def update_debtreduction_chart(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue):
    return update_debtreduction_chart_logic(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue)

@app.callback(
    Output('industries_s', 'children'),
    [
        Input('cluster-filter', 'value'),
        Input('industry-filter', 'value'),
        Input('revenue-trend-filter', 'value'),
        Input('employees-filter', 'value'),
        Input('liquidity-filter', 'value'),
        Input('short-term-debt-filter', 'value'),
        Input('long-term-debt-filter', 'value'),
        Input('total-revenue-filter', 'value')
    ]
)
def update_sector_chart(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue):
    return update_sector_chart_logic(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue)

#################################### TABLE ####################################
# Callback para validar el archivo cargado
@dash.callback(
    Output("upload-alert", "is_open"),
    Output("upload-alert", "children"),
    Output("upload-alert", "color"),
    Output("process-button", "disabled"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    prevent_initial_call=True,
)
def validate_upload(contents, filename):
    if not contents:
        return True, "No se ha cargado ningún archivo.", "danger", True

    try:
        # Decodificar el archivo subido
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)

        # Validar que sea un archivo Excel
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            pd.read_excel(BytesIO(decoded))  # Envolver en BytesIO
            return True, "Archivo válido cargado correctamente.", "success", False
        else:
            return True, "El archivo no es un Excel válido. Intente nuevamente.", "danger", True
    except Exception as e:
        return True, f"Error al procesar el archivo: {str(e)}", "danger", True

# Callback para procesar los datos
@dash.callback(
    Output("result-table-container", "children"),
    Output("download-button", "disabled"),
    Output("processed-data", "data"),
    Input("process-button", "n_clicks"),
    State("upload-data", "contents"),
    State("upload-data", "filename"),
    prevent_initial_call=True,
)
def process_file(n_clicks, contents, filename):
    if not contents:
        return html.Div("No se ha cargado ningún archivo."), True, None

    # Decodificar y procesar el archivo
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)

    try:
        df = pd.read_excel(BytesIO(decoded), skiprows=7)

        df = df[[
            "Company",
            "Cash and Cash Equivalents",    
            "Export",
            "Import",
            "Industry (NAICS)",
            "Long term Debt",
            "Net Sales Revenue Trend (%)",
            "Number of Employees",
            "Operating Profit Trend (%)",
            "Property, plant and equipment",
            "Return on Assets (ROA) (%)",
            "Return on Equity (ROE) (%)",
            "Quick Ratio (x)",
            "Short Term Debt",      
            "Total operating revenue",
        ]]
        df = df.dropna()
        df_input = df.to_dict(orient="records")
        URL = "http://0.0.0.0:8000/"
        result_total = consume_classifier_api(URL, df_input)
        df_result = pd.DataFrame(result_total)

        # Crear tabla Dash
        table = DataTable(
            columns=[{"name": col, "id": col} for col in df_result.columns],
            data=df_result.to_dict("records"),
            style_table={"overflowX": "auto"},
        )

        return table, False, df_result.to_dict("records")
    except Exception as e:
        return html.Div(f"Error al procesar el archivo: {str(e)}"), True, None

# Callback para descargar el archivo procesado
@dash.callback(
    Output("download-dataframe-csv", "data"),
    Input("download-button", "n_clicks"),
    State("processed-data", "data"),
    prevent_initial_call=True,
)
def download_file(n_clicks, data):
    if not data:
        return None

    try:
        df = pd.DataFrame(data)
        return dcc.send_data_frame(df.to_csv, "datos_procesados.csv", index=False)
    except Exception as e:
        return None


if __name__ == "__main__":
    # app.run(debug=True) # For local
    app.run_server(host="0.0.0.0", port="8050") # For compose!!!

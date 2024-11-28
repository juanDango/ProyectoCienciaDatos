import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html

from components.filters.cluster import cluster_filter
from components.filters.industry import industry_filter
from components.filters.revenue_trend import revenue_trend_filter
from components.filters.employees import employees_filter
from components.filters.liquidity import liquidity_filter
from components.filters.long_term_debt import long_term_debt_filter
from components.filters.short_term_debt import short_term_debt_filter
from components.filters.total_revenue import total_revenue_filter
from components.charts.high_income import high_income_chart
from components.charts.sector_income import sector_income_chart
from components.charts.roa_roe import roa_roe_chart
from components.charts.liquidity import liquidity_chart
from components.charts.opportunities import opportunities_chart
from components.charts.operational_capacity import operational_capacity_chart
from components.charts.debt_reduction import debt_reduction_chart
from components.charts.high_debt import high_debt_chart

dash.register_page(__name__, path="/")

data = pd.read_json("datos/complete_payload.json")

layout = dbc.Container(
    [
        html.Div(
            className="content",
            children=[
                # Left menu for filters
                html.Div(
                    className="left_menu",
                    children=[
                        html.Div(
                            className="grid_left",
                            children=[
                                dbc.Row(
                                    html.H4("FILTROS", className="text-center"),
                                    class_name="left_div div1_left",
                                ),
                                dbc.Row(
                                    html.Div([
                                        html.Label("Cluster:", className="filter-label"),
                                        cluster_filter()
                                    ]),
                                    class_name="left_div div2_left",
                                ),
                                dbc.Row(
                                    html.Div([
                                        html.Label("Sector Industrial:", className="filter-label"),
                                        industry_filter()
                                    ]),
                                    class_name="left_div div3_left",
                                ),
                                dbc.Row(
                                    html.Div([
                                        html.Label("Tendencia de Ingresos Operativos (%):", className="filter-label"),
                                        revenue_trend_filter()
                                    ]),
                                    class_name="left_div div4_left",
                                ),
                                dbc.Row(
                                    html.Div([
                                        html.Label("Número de Empleados:", className="filter-label"),
                                        employees_filter()
                                    ]),
                                    class_name="left_div div5_left",
                                ),
                                dbc.Row(
                                    html.Div([
                                        html.Label("Liquidez (Quick Ratio):", className="filter-label"),
                                        liquidity_filter()
                                    ]),
                                    class_name="left_div div6_left",
                                ),
                                dbc.Row(
                                    html.Div([
                                        html.Label("Deuda a Largo Plazo:", className="filter-label"),
                                        long_term_debt_filter()
                                    ]),
                                    class_name="left_div div7_left",
                                ),
                                dbc.Row(
                                    html.Div([
                                        html.Label("Deuda a Corto Plazo:", className="filter-label"),
                                        short_term_debt_filter()
                                    ]),
                                    class_name="left_div div8_left",
                                ),
                                dbc.Row(
                                    html.Div([
                                        html.Label("Ingresos Totales (USD):", className="filter-label"),
                                        total_revenue_filter()
                                    ]),
                                    class_name="left_div div9_left",
                                ),
                            ],
                        ),
                    ],
                ),
                # Right content for the main dashboard
                html.Div(
                    className="right_content",
                    children=[
                        html.Div(
                            className="grid",
                            children=[
                                # Gráfico 1: Oportunidades por rentabilidad
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        html.Div(opportunities_chart(data))
                                    ],
                                ),
                                # Gráfico 2: ROA y ROE superiores
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        html.Div(roa_roe_chart(data))
                                    ],
                                ),
                                # Gráfico 3: Empresas con ingresos altos
                                dbc.Row(
                                    className="right_div",
                                    children=[
                                        html.Div(high_income_chart(data))
                                    ],
                                ),
                                # Gráfico 4: Distribución de liquidez
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        html.Div(liquidity_chart(data))
                                    ],
                                ),
                                # Gráfico 5: Endeudamiento preocupante
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        html.Div(high_debt_chart(data))
                                    ],
                                ),
                                # Gráfico 6: Capacidad operativa
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        html.Div(operational_capacity_chart(data))
                                    ],
                                ),
                                # Gráfico 7: Reducción de deuda
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        html.Div(debt_reduction_chart(data))
                                    ],
                                ),
                                # Gráfico 8: Sectores con mayores ingresos
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        html.Div(sector_income_chart(data))
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
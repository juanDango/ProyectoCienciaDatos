import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from components.charts.debt_reduction import DebtReductionChart
from components.charts.high_debt import HighDebtChart
from components.charts.high_income import HighIncomeChart
from components.charts.liquidity import LiquidityChart
from components.charts.operational_capacity import OperationalCapacityChart
from components.charts.opportunities import OpportunitiesChart
from components.charts.roa_roe import RoaRoeChart
from components.charts.sector_income import SectorIncomeChart
from components.filters.cluster import cluster_filter
from components.filters.employees import employees_filter
from components.filters.industry import industry_filter
from components.filters.liquidity import liquidity_filter
from components.filters.long_term_debt import long_term_debt_filter
from components.filters.revenue_trend import revenue_trend_filter
from components.filters.short_term_debt import short_term_debt_filter
from components.filters.total_revenue import total_revenue_filter
from utils.data_loader import DataLoader

dash.register_page(__name__, path="/")
data_instance = DataLoader(file_path="datos/complete_payload.json")


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
                                        dcc.Store(id='data-loaded', data=True),
                                        html.Label("Cluster:", className="filter-label"),
                                        cluster_filter()
                                    ]),
                                    class_name="left_div div2_left",
                                ),
                                dbc.Row(
                                    html.Div([
                                        dcc.Store(id='data-loaded', data=True),
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
                                        dbc.Card(
                                            class_name="card_figure",
                                            id="opportunities",
                                            children=OpportunitiesChart(
                                                id_graph="opportunities-chart",
                                                data=data_instance.get_data()
                                            ).render()
                                        )
                                    ],
                                ),
                                # Gráfico 2: ROA y ROE superiores
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        dbc.Card(
                                            class_name="card_figure",
                                            id="roa_roe",
                                            children=RoaRoeChart(
                                                id_graph="roa-roe-chart",
                                                data=data_instance.get_data()
                                            ).render()
                                        )
                                    ],
                                ),
                                # Gráfico 3: Empresas con ingresos altos
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        dbc.Card(
                                            class_name="card_figure",
                                            id="revenue",
                                            children=HighIncomeChart(
                                                id_graph="high-income-chart",
                                                data=data_instance.get_data()
                                            ).render()
                                        )
                                    ],
                                ),
                                # Gráfico 4: Distribución de liquidez
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        dbc.Card(
                                            class_name="card_figure",
                                            id="quick",
                                            children=LiquidityChart(
                                                id_graph="liquidity-chart",
                                                data=data_instance.get_data()
                                            ).render()
                                        )
                                    ],
                                ),
                                # Gráfico 5: Endeudamiento preocupante
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        dbc.Card(
                                            class_name="card_figure",
                                            id="highdebt",
                                            children=HighDebtChart(
                                                id_graph="high-debt-chart",
                                                data=data_instance.get_data()
                                            ).render()
                                        )
                                    ],
                                ),
                                # Gráfico 6: Capacidad operativa
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        dbc.Card(
                                            class_name="card_figure",
                                            id="o_revenue",
                                            children=OperationalCapacityChart(
                                                id_graph="operational-capacity-chart",
                                                data=data_instance.get_data()
                                            ).render()
                                        )
                                    ],
                                ),
                                # Gráfico 7: Reducción de deuda
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        dbc.Card(
                                            class_name="card_figure",
                                            id="debt_reduction",
                                            children=DebtReductionChart(
                                                id_graph="debt-reduction-chart",
                                                data=data_instance.get_data()
                                            ).render()
                                        )
                                    ],
                                ),
                                # Gráfico 8: Sectores con mayores ingresos
                                dbc.Row(
                                    class_name="right_div",
                                    children=[
                                        dbc.Card(
                                            class_name="card_figure",
                                            id="industries_s",
                                            children=SectorIncomeChart(
                                                id_graph="sector-income-chart",
                                                data=data_instance.get_data()
                                            ).render()
                                        )
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
    fluid=True,
    class_name="px-0",
)
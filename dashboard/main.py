import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output

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


if __name__ == "__main__":
    app.run(debug=True)
    # app.run_server(host="0.0.0.0", port="8050") # For compose!!!

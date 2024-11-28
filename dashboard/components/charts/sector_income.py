from dash import dcc
import plotly.express as px

def sector_income_chart(data):
    fig = px.pie(
        data,
        names='NAICS_Group',
        values='Total operating revenue',
        title='Distribución de Ingresos por Sector',
    )
    return dcc.Graph(id='sector-income-chart', figure=fig)

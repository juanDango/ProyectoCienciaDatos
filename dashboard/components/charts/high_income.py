from dash import dcc
import plotly.express as px


def high_income_chart(data):
    filtered_data = data[data['Total operating revenue'] > 1e6]
    all_clusters = sorted(data['cluster'].unique())
    fig = px.bar(
        filtered_data.groupby('cluster', as_index=False).sum(),
        x='cluster',
        y='Total operating revenue',
        # color='cluster',
        title='Ingresos Operativos por Clúster (> 1M USD)',
        labels={'Total operating revenue': 'Ingresos Totales (USD)', 'Cluster': 'Clúster'}
    )
    fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)
    return dcc.Graph(id='high-income-chart', figure=fig)

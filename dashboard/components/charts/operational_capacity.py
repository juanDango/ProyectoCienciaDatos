from dash import dcc
import plotly.express as px

def operational_capacity_chart(data):
    aggregated_data = data.groupby('cluster', as_index=False)['Employees'].sum()
    all_clusters = sorted(data['cluster'].unique())

    fig = px.bar(
        aggregated_data,
        x='cluster',
        y='Employees',
        title='Capacidad Operativa Total (Sumatoria del número de Empleados) por Clúster',
        labels={
            'Cluster': 'Clúster',
            'Employees': 'Número de Empleados'
        }
    )
    fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)
    return dcc.Graph(id='operational-capacity-chart', figure=fig)


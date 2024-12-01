import plotly.express as px
from dash import dcc


class OperationalCapacityChart:
    def __init__(self, data, id_graph:str = "operational-capacity-chart"):
        """
        Clase para crear un gráfico de high-income basado en datos agregados por clúster.
        :param data: DataFrame.
        """
        self.data = data
        self.id_graph = id_graph

    def render(self):
        aggregated_data = self.data.groupby('cluster', as_index=False)['Employees'].sum()
        all_clusters = sorted(self.data['cluster'].unique())

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
        return dcc.Graph(id=self.id_graph, figure=fig)


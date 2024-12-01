import plotly.express as px
from dash import dcc


class HighIncomeChart:
    def __init__(self, data, id_graph:str = "high-income-chart"):
        """
        Clase para crear un gráfico de high-income basado en datos agregados por clúster.
        :param data: DataFrame.
        """
        self.data = data
        self.id_graph = id_graph

    def render(self):
        """
        Genera y devuelve un objeto dcc.Graph con el gráfico.
        :return: dcc.Graph
        """
        filtered_data = self.data[self.data['Total operating revenue'] > 1e6]
        all_clusters = sorted(self.data['cluster'].unique())
        fig = px.bar(
            filtered_data.groupby('cluster', as_index=False).sum(),
            x='cluster',
            y='Total operating revenue',
            title='Ingresos Operativos por Clúster (> 1M USD)',
            labels={'Total operating revenue': 'Ingresos Totales (USD)', 'Cluster': 'Clúster'}
        )
        fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)
        return dcc.Graph(id=self.id_graph, figure=fig)

import plotly.express as px
from dash import dcc


class LiquidityChart:
    def __init__(self, data, id_graph:str = "liquidity-chart"):
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
        aggregated_data = self.data.groupby('cluster', as_index=False)['Quick Ratio (x)'].mean()
        all_clusters = sorted(self.data['cluster'].unique())

        fig = px.bar(
            aggregated_data,
            x='cluster',
            y='Quick Ratio (x)',
            title='Distribución Media de Liquidez por Clúster',
            labels={'Quick Ratio (x)': 'Quick Ratio', 'Cluster': 'Clúster'},
        )
        fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)
        return dcc.Graph(id=self.id_graph, figure=fig)

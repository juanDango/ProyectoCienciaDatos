import plotly.express as px
from dash import dcc


class HighDebtChart:
    def __init__(self, data, id_graph:str = "high-debt-chart"):
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
        self.data['Debt Ratio'] = self.data['Long term Debt'] / (self.data['Long term Debt'] + self.data['Short Term Debt'])
        all_clusters = sorted(self.data['cluster'].unique())
        fig = px.box(
            self.data,
            x='cluster',
            y='Debt Ratio',
            color='cluster',
            title='Distribución de Endeudamiento por Clúster',
            labels={'Debt Ratio': 'Relación de Deuda'}
        )
        fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)
        fig.update_layout(showlegend=False)
        return dcc.Graph(id=self.id_graph, figure=fig)

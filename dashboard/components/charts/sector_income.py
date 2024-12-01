import plotly.express as px
from dash import dcc


class SectorIncomeChart:
    def __init__(self, data, id_graph:str = 'sector-income-chart'):
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
        fig = px.pie(
            self.data,
            names='NAICS_Group',
            values='Total operating revenue',
            title='Distribución de Ingresos por Sector',
        )
        return dcc.Graph(id=self.id_graph, figure=fig)

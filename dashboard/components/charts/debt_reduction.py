import plotly.express as px
from dash import dcc


class DebtReductionChart:
    def __init__(self, data, id_graph:str = "debt-reduction-chart"):
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
        aggregated_data = self.data.groupby('cluster', as_index=False)[
            ['Short Term Debt', 'Long term Debt']
        ].sum()
        all_clusters = sorted(self.data['cluster'].unique())

        fig = px.bar(
            aggregated_data.melt(id_vars='cluster', var_name='Debt Type', value_name='Amount'),
            x='cluster',
            y='Amount',
            color='Debt Type',
            title='Deuda a Corto y Largo Plazo por Clúster',
            barmode='group',
            labels={
                'cluster': 'Clúster',
                'Amount': 'Monto (USD)',
                'Debt Type': 'Tipo de Deuda'
            }
        )
        fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)

        return dcc.Graph(id=self.id_graph, figure=fig)


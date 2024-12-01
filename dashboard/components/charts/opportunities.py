from dash import dcc
import plotly.graph_objects as go

class OpportunitiesChart:
    def __init__(self, data, id_graph:str = "opportunities-chart"):
        """
        Clase para crear un gráfico de oportunidades basado en datos agregados por clúster.
        :param data: DataFrame que contiene las columnas 'cluster',
                     'Net Sales Revenue Trend (%)', 'Operating Profit Trend (%)',
                     y 'Total operating revenue'.
        """
        self.data = data
        self.id_graph = id_graph

    def render(self):
        """
        Genera y devuelve un objeto dcc.Graph con el gráfico de oportunidades.
        :return: dcc.Graph
        """
        aggregated_data = self.data.groupby('cluster', as_index=False)[
            ['Net Sales Revenue Trend (%)', 'Operating Profit Trend (%)', 'Total operating revenue']
        ].mean()
        all_clusters = sorted(self.data['cluster'].unique())

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=aggregated_data['cluster'],
                y=aggregated_data['Operating Profit Trend (%)'],
                name='Tendencia de Utilidad Operativa (%)',
                marker=dict(color='blue'),
                yaxis='y1',
            )
        )

        fig.add_trace(
            go.Scatter(
                x=aggregated_data['cluster'],
                y=aggregated_data['Net Sales Revenue Trend (%)'],
                name='Tendencia de Ingresos (%)',
                mode='lines+markers',
                line=dict(color='red'),
                yaxis='y2',
            )
        )

        fig.update_layout(
            title='Oportunidades de Rentabilidad y Crecimiento por Clúster',
            xaxis=dict(title='Clúster'),
            yaxis=dict(
                title='Tendencia de Utilidad Operativa (%)',
                titlefont=dict(color='blue'),
                tickfont=dict(color='blue'),
            ),
            yaxis2=dict(
                title='Tendencia de Ingresos (%)',
                titlefont=dict(color='red'),
                tickfont=dict(color='red'),
                overlaying='y',
                side='right',
            ),
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            margin=dict(l=40, r=40, t=40, b=40),
            template='plotly_white',
        )

        # Ordenar categorías del eje x
        fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)

        return dcc.Graph(id=self.id_graph, figure=fig)

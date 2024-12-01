import plotly.graph_objects as go
from dash import dcc


class RoaRoeChart:
    def __init__(self, data, id_graph:str = "roa-roe-chart"):
        """
        Clase para crear un gráfico de roa-roe basado en datos agregados por clúster.
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
            ['Return on Assets (ROA) (%)', 'Return on Equity (ROE) (%)']
        ].mean()
        all_clusters = sorted(self.data['cluster'].unique())

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=aggregated_data['cluster'],
                y=aggregated_data['Return on Assets (ROA) (%)'],
                name='ROA (%)',
                marker=dict(color='blue'),
                yaxis='y1',
            )
        )

        fig.add_trace(
            go.Scatter(
                x=aggregated_data['cluster'],
                y=aggregated_data['Return on Equity (ROE) (%)'],
                name='ROE (%)',
                mode='lines+markers',
                line=dict(color='red'),
                yaxis='y2',
            )
        )

        fig.update_layout(
            title='Relación ROA y ROE por Clúster',
            xaxis=dict(title='Clúster'),
            yaxis=dict(
                title='ROA (%)',
                titlefont=dict(color='blue'),
                tickfont=dict(color='blue'),
            ),
            yaxis2=dict(
                title='ROE (%)',
                titlefont=dict(color='red'),
                tickfont=dict(color='red'),
                overlaying='y',
                side='right',
            ),
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            margin=dict(l=40, r=40, t=40, b=40),
            template='plotly_white',
        )
        fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)

        return dcc.Graph(id=self.id_graph, figure=fig)

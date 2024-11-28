from dash import dcc
import plotly.graph_objects as go

def roa_roe_chart(data):
    # Agrupar datos por clúster
    aggregated_data = data.groupby('cluster', as_index=False)[
        ['Return on Assets (ROA) (%)', 'Return on Equity (ROE) (%)']
    ].mean()
    all_clusters = sorted(data['cluster'].unique())

    # Crear figura con doble eje Y
    fig = go.Figure()

    # Agregar datos para ROA
    fig.add_trace(
        go.Bar(
            x=aggregated_data['cluster'],
            y=aggregated_data['Return on Assets (ROA) (%)'],
            name='ROA (%)',
            marker=dict(color='blue'),
            yaxis='y1',
        )
    )

    # Agregar datos para ROE
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

    # Configuración del diseño
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
    return dcc.Graph(id='roa-roe-chart', figure=fig)

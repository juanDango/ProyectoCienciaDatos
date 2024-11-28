from dash import dcc
import plotly.express as px

def liquidity_chart(data):
    aggregated_data = data.groupby('cluster', as_index=False)['Quick Ratio (x)'].mean()
    all_clusters = sorted(data['cluster'].unique())

    fig = px.bar(
        aggregated_data,
        x='cluster',
        y='Quick Ratio (x)',
        title='Distribución Media de Liquidez por Clúster',
        labels={'Quick Ratio (x)': 'Quick Ratio', 'Cluster': 'Clúster'},
    )
    fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)
    return dcc.Graph(id='liquidity-chart', figure=fig)


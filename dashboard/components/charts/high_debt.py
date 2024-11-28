from dash import dcc
import plotly.express as px

def high_debt_chart(data):
    data['Debt Ratio'] = data['Long term Debt'] / (data['Long term Debt'] + data['Short Term Debt'])
    all_clusters = sorted(data['cluster'].unique())
    fig = px.box(
        data,
        x='cluster',
        y='Debt Ratio',
        color='cluster',
        title='Distribución de Endeudamiento por Clúster',
        labels={'Debt Ratio': 'Relación de Deuda'}
    )
    fig.update_xaxes(type='category', categoryorder='array', categoryarray=all_clusters)
    fig.update_layout(showlegend=False)
    return dcc.Graph(id='high-debt-chart', figure=fig)

from dash import dcc
import plotly.express as px

def debt_reduction_chart(data):
    aggregated_data = data.groupby('cluster', as_index=False)[
        ['Short Term Debt', 'Long term Debt']
    ].sum()
    all_clusters = sorted(data['cluster'].unique())

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

    return dcc.Graph(id='debt-reduction-chart', figure=fig)


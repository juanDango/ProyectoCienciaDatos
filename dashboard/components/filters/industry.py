from dash import dcc

def industry_filter():
    industries = [
        "Natural Gas Extraction", "Grocery Stores", "Electric Power Generation",
        "Coal Mining", "Health and Welfare Funds", "Wireless Telecommunications Carriers",
        "Petroleum and Petroleum Products Merchant Wholesalers"
    ]  # Reemplazar con la lista de industrias en tus datos
    return dcc.Dropdown(
        id='industry-filter',
        options=[{'label': industry, 'value': industry} for industry in industries],
        placeholder='Select Industry',
        multi=True
    )

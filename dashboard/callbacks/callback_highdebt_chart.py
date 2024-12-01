from components.charts.high_debt import HighDebtChart
from utils.data_loader import DataLoader


def update_highdebt_chart_logic(clusters, industries, revenue_trend, employees, liquidity, s_debt, l_debt, t_revenue):
    full_data = DataLoader(file_path="datos/complete_payload.json")
    filtered_data = full_data.get_data().copy()
    if clusters:
        filtered_data = filtered_data[filtered_data['cluster'].isin(clusters)]
    if industries:
        filtered_data = filtered_data[filtered_data['NAICS_Group'].isin(industries)]
    if revenue_trend:
        filtered_data = filtered_data[
            (filtered_data['Net Sales Revenue Trend (%)'] >= revenue_trend[0]) &
            (filtered_data['Net Sales Revenue Trend (%)'] <= revenue_trend[1])
        ]
    if employees:
        filtered_data = filtered_data[
            (filtered_data['Employees'] >= employees[0]) &
            (filtered_data['Employees'] <= employees[1])
        ]
    if liquidity:
        filtered_data = filtered_data[
            (filtered_data['Quick Ratio (x)'] >= liquidity[0]) &
            (filtered_data['Quick Ratio (x)'] <= liquidity[1])
        ]
    if s_debt:
        filtered_data = filtered_data[
            (filtered_data['Short Term Debt'] >= s_debt[0]) &
            (filtered_data['Short Term Debt'] <= s_debt[1])
        ]
    if l_debt:
        filtered_data = filtered_data[
            (filtered_data['Long term Debt'] >= l_debt[0]) &
            (filtered_data['Long term Debt'] <= l_debt[1])
        ]
    if t_revenue:
        filtered_data = filtered_data[
            (filtered_data['Total operating revenue'] >= t_revenue[0]) &
            (filtered_data['Total operating revenue'] <= t_revenue[1])
        ]
    else:
        filtered_data = filtered_data
    
    return HighDebtChart(
        data=filtered_data,
    ).render()

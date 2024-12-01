from utils.data_loader import DataLoader


def industry_filter_callback_logic():
    data = DataLoader(file_path="datos/complete_payload.json").get_data()
    available_NAICS_Groups = data['NAICS_Group'].unique()
    options = [{'label': f'{i}', 'value': i} for i in sorted(available_NAICS_Groups)]
    return options
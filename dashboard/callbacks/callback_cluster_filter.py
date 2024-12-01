from utils.data_loader import DataLoader


def cluster_filter_callback_logic():
    data = DataLoader(file_path="datos/complete_payload.json").get_data()
    available_clusters = data['cluster'].unique()
    options = [{'label': f'Cluster {i}', 'value': i} for i in sorted(available_clusters)]
    return options
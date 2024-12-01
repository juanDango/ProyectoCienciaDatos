import os

import pandas as pd


class DataLoader:
    """
    Clase para manejar la carga y actualización de datos dinámicamente.
    """
    def __init__(self, file_path="datos/complete_payload.json"):
        self.file_path = file_path
        self.data = None
        self.load_data()

    def load_data(self):
        """
        Carga los datos desde el archivo especificado.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"El archivo {self.file_path} no existe.")
        try:
            self.data = pd.read_json(self.file_path)
            # print(f"Datos cargados desde {self.file_path}")
        except Exception as e:
            raise ValueError(f"Error al cargar los datos: {e}")

    def get_data(self):
        """
        Devuelve los datos actuales.
        """
        return self.data

    def set_data(self, data):
        """
        Asigna los datos.
        """
        self.data = data
        return self.data

    def reload_data(self):
        """
        Recarga los datos desde el archivo en caso de cambios.
        """
        self.load_data()
        print("Datos recargados.")

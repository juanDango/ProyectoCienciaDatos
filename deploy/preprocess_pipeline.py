import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import re
import joblib

naics_map = {
        '11': 'Agricultura, Pesca y Minería',
        '21': 'Minería y Extracción',
        '22': 'Servicios Públicos',
        '23': 'Construcción',
        '31': 'Manufactura',
        '32': 'Manufactura',
        '33': 'Manufactura',
        '42': 'Comercio Mayorista',
        '44': 'Comercio Minorista',
        '45': 'Comercio Minorista',
        '48': 'Transporte y Almacenamiento',
        '49': 'Transporte y Almacenamiento',
        '51': 'Información y Tecnología',
        '52': 'Finanzas y Seguros',
        '53': 'Bienes Raíces',
        '54': 'Servicios Profesionales y Técnicos',
        '55': 'Administración de Empresas',
        '56': 'Servicios Administrativos y Apoyo',
        '61': 'Educación',
        '62': 'Salud y Asistencia Social',
        '71': 'Arte, Entretenimiento y Recreación',
        '72': 'Alojamiento y Servicios Alimenticios',
        '81': 'Otros Servicios',
        '92': 'Administración Pública'
}

# 1. Carga de Datos
def load_data(file_path):
    return pd.DataFrame(file_path)

# 2. Selección Inicial de Variables (Basada en EDA)
def initial_variable_selection(df):
    # Variables seleccionadas según el EDA
    selected_variables = [
        "Company",
        "Cash and Cash Equivalents",    
        "Export",
        "Import",
        "Industry (NAICS)",
        "Long term Debt",
        "Net Sales Revenue Trend (%)",
        "Number of Employees",
        "Operating Profit Trend (%)",
        "Property, plant and equipment",
        "Return on Assets (ROA) (%)",
        "Return on Equity (ROE) (%)",
        "Quick Ratio (x)",
        "Short Term Debt",      
        "Total operating revenue",
    ]
    return df[selected_variables]

def clean_data(df):
    # Identificar columnas categóricas y numéricas
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    
    # Imputación para columnas numéricas
    if len(numeric_columns) > 0:
        numeric_imputer = SimpleImputer(strategy='median')
        df[numeric_columns] = pd.DataFrame(
            numeric_imputer.fit_transform(df[numeric_columns]),
            columns=numeric_columns,
            index=df.index
        )
    
    # Imputación para columnas categóricas
    if len(categorical_columns) > 0:
        categorical_imputer = SimpleImputer(strategy='most_frequent')
        df[categorical_columns] = pd.DataFrame(
            categorical_imputer.fit_transform(df[categorical_columns]),
            columns=categorical_columns,
            index=df.index
        )
    
    # Eliminar filas que aún contengan valores nulos
    df.dropna(inplace=True)
    return df


# 4. Transformación de Datos
def transform_data(df):
    # Evitar divisiones por cero
    df['Property, plant and equipment'] = df['Property, plant and equipment'].replace(0, np.nan)
    df['Debt_to_Assets'] = (df['Long term Debt'] + df['Short Term Debt']) / df['Property, plant and equipment']
    df['Relative_Growth'] = df['Net Sales Revenue Trend (%)'] - df['Operating Profit Trend (%)']
    
    # Reemplazar infinitos y NaN generados
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)  # Rellenar valores faltantes con 0 después de las transformaciones
    return df

# 5. Preprocesamiento y Normalización
def prepare_pipeline(df):
    # Identificar columnas categóricas y numéricas
    categorical_features = df.select_dtypes(include=['object']).columns.tolist()
    numeric_features = df.select_dtypes(include=['float64']).columns.tolist()
    
    # Preprocesamiento para variables numéricas
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])
    
    # Preprocesamiento para variables categóricas
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    # Combinar preprocesamiento
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ],
        remainder='drop'  # Eliminar columnas no especificadas
    )
    return preprocessor

# Función para extraer los países y porcentajes con expresiones regulares
def extract_countries_values_regex(column):
    country_dict = {}
    for row in column.dropna():
        # Buscar todas las ocurrencias del patrón 'PAIS (Porcentaje%)' o 'PAIS'
        matches = re.findall(r'([A-Za-z\s]+)(?:\s*\(([\d.]+)%\))?', row)
        for country, percentage in matches:
            country = country.strip()
            if percentage:
                percentage = float(percentage)
            else:
                percentage = 0.0  # Si no hay porcentaje, asignamos 0.0
            country_dict[country] = country_dict.get(country, 0) + percentage
    return country_dict

# Función para extraer los porcentajes de un item
def extract_percentage_from_item(item):
    try:
        # Verificar si el item contiene un porcentaje, de lo contrario devolver 0.0
        if '(' in item and ')' in item:
            return float(item.split('(')[1].replace('%', '').replace(')', '').strip())
        else:
            return 0.0
    except (IndexError, ValueError):
        return 0.0  # Manejo de errores si no es posible convertir el porcentaje

def import_export_preprocessing(datos):
    # Empleados
    datos['Employees'] = datos['Number of Employees'].str.extract(r'([\d,]+)\s\(\d{4}\)')
    datos['Employees'] = datos['Employees'].str.replace(',', '').replace('', np.nan).astype(float)
 
    # Lista de países específicos para importación y exportación
    countries = ['CN', 'US', 'EC', 'MX', 'ES', 'DE', 'BR', 'PE', 'IT', 'PA']
 
    # Generar nuevas columnas solo para los países especificados
    for country in countries:
        datos[f'Export_{country}'] = datos['Export']. \
            apply(
                lambda x: extract_percentage_from_item(
                    [item for item in x.split(',') if country in item][0]
                ) if isinstance(x, str) and any(country in item for item in x.split(',')) else 0.0
            )
        datos[f'Import_{country}'] = datos['Import']. \
            apply(
                lambda x: extract_percentage_from_item(
                    [item for item in x.split(',') if country in item][0]
                ) if isinstance(x, str) and any(country in item for item in x.split(',')) else 0.0
            )
    # Eliminar columnas no necesarias
    datos = datos.drop(["Import", "Export", "Number of Employees"], axis=1)
 
    return datos


def get_first_NAICS(datos: pd.DataFrame):
    datos['Industry (NAICS)'] = datos['Industry (NAICS)'].fillna('').astype(str)
    datos['First_Sector'] = datos['Industry (NAICS)'].str.split(';').str[0]

    # Extraer los primeros dos dígitos de los códigos NAICS
    datos['NAICS_Sector'] = datos['First_Sector'].str.extract(r'\((\d{2})\d*\)')[0]
    # Mapear los sectores principales utilizando el diccionario
    datos['NAICS_Group'] = datos['NAICS_Sector'].map(naics_map)
    datos = datos.drop(['First_Sector', 'Industry (NAICS)', 'NAICS_Sector'], axis=1)

    return datos


# Pipeline Completo
def run_pipeline(file_path):
    # Carga de datos
    data = load_data(file_path)
    
    print(data.head(5))
    
    # Selección inicial de variables
    selected_data = initial_variable_selection(data)

    import_export_adjusted = import_export_preprocessing(selected_data)

    first_NAIC = get_first_NAICS(import_export_adjusted)
    
    # Limpieza de datos
    clean_data_df = clean_data(first_NAIC)
    
    # Transformación de datos
    transformed_data = transform_data(clean_data_df)

    # Reinicia el índice para evitar que sea considerado una columna
    transformed_data = transformed_data.reset_index(drop=True)

    preprocessor = joblib.load('preprocessor.pkl')
    
    processed_data = preprocessor.transform(transformed_data[transformed_data.columns[1:]])
    
    return processed_data, transformed_data
        
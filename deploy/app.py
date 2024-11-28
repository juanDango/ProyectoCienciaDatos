from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from typing import List, Dict
from preprocess_pipeline import run_pipeline
from fastapi.responses import JSONResponse
 

# Cargar el modelo K-Means guardado como joblib
model = joblib.load("kmeans_model.joblib")

# Crear la aplicación FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de clasificación de empresas funcionando correctamente"}

@app.post("/classify/")
def classify_companies(companies: List[Dict]):
    """
    Recibe una lista de empresas en formato JSON, las procesa y las clasifica en clústeres.
    """
    try:
        # Preprocesar los datos de la empresa
        processed_data = run_pipeline(companies)
            
        # Convertir los datos preprocesados a un array para el modelo
        # (Asegúrate de que las claves y el orden coincidan con lo esperado por el modelo)
        features = np.array([list(processed_data.values())]).reshape(1, -1)
            
        # Realizar la predicción de clúster
        cluster = model.predict(features)[0]
            
        # Agregar el resultado al JSON final
        processed_data["cluster"] = cluster
        json_data = processed_data.to_json(orient="records")
        
        return JSONResponse(content=json_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar los datos: {str(e)}")


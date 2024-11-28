from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from typing import List, Dict
from preprocess_pipeline import run_pipeline
from fastapi.responses import JSONResponse
import uvicorn
import json
 

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
        processed_data, transformed = run_pipeline(companies)
            
        # Realizar la predicción de clúster
        cluster = model.predict(processed_data)
            
        # Agregar el resultado al JSON final
        transformed["cluster"] = cluster
        json_string = transformed.to_json(orient="records")
        json_data = json.loads(json_string)  # Convertir la cadena JSON a un objeto Python (lista de diccionarios)

        # Devolver la respuesta JSON
        return JSONResponse(content=json_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar los datos: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Importa el middleware CORS
from typing import List
from app.models import Data, DataResponse
from app.schematics import insert_data, get_all_data, get_data_by_group_id
from app.database import create_table

create_table()

# Crear la instancia de la app FastAPI
app = FastAPI(
    title="APIESP32",
    description="API para ESP32",
    version="0.1"
)

# Lista de orígenes permitidos (ajusta según tu frontend)
origins = [
    "http://localhost",
    "http://localhost:8080",  # Ajusta esto según el puerto de tu frontend
    "http://192.168.80.12:8082"  # El puerto de tu frontend
]

# Configura el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite cualquier método (GET, POST, etc.)
    allow_headers=["*"],  # Permite cualquier header
)

@app.post('/api/prototype/insert')
def method_name(data:Data):
    try:
        id= insert_data(data)
        return{**data.dict(), "id":id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/api/prototype/view', response_model=List[DataResponse])
def read_data():
    try:
        data = get_all_data()
        if not data:
            raise HTTPException(status_code=404, detail="No data found")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.get('/api/prototype/view/{group_id}', response_model=List[DataResponse])
def read_data(group_id: str):
    try:
        # Filtrar los datos por group_id
        data = get_data_by_group_id(group_id)
        
        if not data:
            raise HTTPException(status_code=404, detail="No data found for this group_id")
        
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

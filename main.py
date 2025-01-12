from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  
from typing import List
from app.models import Data, DataResponse
from app.schematics import insert_data, get_all_data, get_data_by_group_id
from app.database import create_table

create_table()

app = FastAPI(
    title="APIESP32",
    description="API para ESP32",
    version="0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
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

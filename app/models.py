from pydantic import BaseModel  

class Data (BaseModel):
    group_id: str
    time: float
    displacement: float
    velocity: float
    acceleration: float

class DataResponse(Data):
    id:int
    

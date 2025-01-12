import sqlite3 as db
from app.models import Data, DataResponse
from typing import List

DB_NAME = 'APIESP32.db'

def insert_data(data: Data):
    conn = db.connect(database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO data_moviments (
            group_id, 
            time, 
            displacement,
            velocity,
            acceleration
        )
        VALUES (?, ?, ?, ?, ?)
    """, (data.group_id, data.time, data.displacement, data.velocity, data.acceleration))
    conn.commit()
    id = cursor.lastrowid
    conn.close()
    return id

def get_all_data():
    conn = db.connect(database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data_moviments")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "group_id": row[1],
            "time": row[2],
            "displacement": row[3],
            "velocity": row[4],
            "acceleration": row[5]
        }
        for row in rows
    ]
    
def get_data_by_group_id(group_id: str) -> List[Data]:
    try:
        conn = db.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data_moviments WHERE group_id = ?", (group_id,))
        rows = cursor.fetchall()
        conn.close()
        
        result = [
            DataResponse(
                id=row[0],
                group_id=row[1],
                time=row[2],
                displacement=row[3],
                velocity=row[4],
                acceleration=row[5]
            )
            for row in rows
        ]
        return result
    except Exception as e:
        raise Exception(f"Error fetching data by group_id: {str(e)}")
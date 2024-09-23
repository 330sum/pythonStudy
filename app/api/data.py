from fastapi import APIRouter, HTTPException
from app.common import connectionPool
import pandas as pd

router = APIRouter()

async def fetch_data(query: str):
    connection = connectionPool.get_db()  # 연결 가져오기
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        return pd.DataFrame(data, columns=column_names)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        connection.close()  # 연결 닫기

@router.get("/data")
async def read_data():
    query = "SELECT * FROM test"
    datalist = await fetch_data(query)  # 데이터를 가져오는 함수 호출
    print(datalist)
    print('================')
    print(datalist.to_dict(orient='records'))
    return datalist.to_dict(orient='records')  # JSON 형태로 반환
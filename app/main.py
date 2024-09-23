from fastapi import FastAPI, HTTPException
from app.common import connectionPool

from app.api.data import router as data_router  # data.py에서 라우터 가져오기

app = FastAPI(
    title="My API",
    description="This is a sample API server."
)

# 연결 풀 설정
connectionPool.setup_connection_pool()

app.include_router(data_router)  # 라우터 포함

@app.get("/")
async def read_root():
    return {"message": "연결 됐슘듕!! Welcome to the API!!"}

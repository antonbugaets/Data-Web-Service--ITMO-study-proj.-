from fastapi import FastAPI, Request 
import uvicorn
from routers import router

app = FastAPI(
    title="TestApp",
    description=("Study Dev App"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', workers=1, port=3001)


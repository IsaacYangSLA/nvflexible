import uvicorn

from fastapi import Depends, FastAPI

from .internal import admin
from .routers import submissions, s3, health

app = FastAPI(prefix="/api/v1")

app.include_router(submissions.router)
app.include_router(s3.router)
app.include_router(health.router)
app.include_router(admin.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

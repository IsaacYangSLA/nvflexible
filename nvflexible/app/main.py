import uvicorn

from fastapi import Depends, FastAPI

from .internal import admin
from .routers import submissions, s3, health

app = FastAPI()

app_v1 = FastAPI()
# app_v1.include_router(submissions.router)
# app_v1.include_router(s3.router)
# app_v1.include_router(health.router)
app_v1.include_router(admin.router)

app.mount("/api/v1", app_v1)

@app.get("/")
def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

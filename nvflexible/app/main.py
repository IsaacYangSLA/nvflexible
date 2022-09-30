from fastapi import Depends, FastAPI

from .internal import admin
from .routers import submissions, s3, health


app = FastAPI()

# app_v1.include_router(submissions.router)
# app_v1.include_router(s3.router)
# app_v1.include_router(health.router)
app.include_router(admin.router)

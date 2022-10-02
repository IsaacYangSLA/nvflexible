from fastapi import Depends, FastAPI

#from .internal import admin
#from .routers import submissions, s3, health
from .dummy import dummy

app = FastAPI()

# app.include_router(submissions.router)
# app.include_router(s3.router)
# app.include_router(health.router)
# app.include_router(admin.router)
app.include_router(dummy.router)
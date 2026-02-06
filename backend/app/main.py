from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.files import router as files_router
from app.db.session import Base, engine
from app.db import models  # noqa: F401

app = FastAPI(title="3T Sample App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(health_router, prefix="/api/v1")
app.include_router(files_router, prefix="/api/v1")

from fastapi import FastAPI

from database import Base, engine
from students import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CampusCore API"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Student API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }
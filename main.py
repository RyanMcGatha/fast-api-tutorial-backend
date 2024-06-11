from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()



origins = [

    "http://localhost:3000",  
    "https://fast-api-tutorial-backend.vercel.app/",
    "https://fastapi-tutorial.netlify.app"
    "https://fastapi-tutorial.netlify.app/tutorial"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ceos/{ceo_id}", response_model=schemas.CEO)
def read_ceo(ceo_id: int, db: Session = Depends(get_db)):
    db_ceo = crud.get_ceo(db, ceo_id=ceo_id)
    if db_ceo is None:
        raise HTTPException(status_code=404, detail="CEO not found")
    return db_ceo


@app.post("/ceos/{ceo_id}", response_model=schemas.CEO)
def create_ceo(ceo_id: int, ceo: schemas.CEOCreate = Body(...), db: Session = Depends(get_db)):
    created_ceo = crud.create_ceo(db=db, ceo=ceo)
    response = JSONResponse(content=created_ceo)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

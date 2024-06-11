from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
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
    return crud.create_ceo(db=db, ceo=ceo)

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

@app.get("/ceos/id/{ceo_id}", response_model=schemas.CEO)
def read_ceo_by_id(ceo_id: int, db: Session = Depends(get_db)):
    db_ceo = crud.get_ceo_by_id(db, ceo_id=ceo_id)
    if db_ceo is None:
        raise HTTPException(status_code=404, detail="CEO not found")
    return db_ceo

@app.get("/ceos/name/{ceo_name}", response_model=schemas.CEO)
def read_ceo_by_name(ceo_name: str, db: Session = Depends(get_db)):
    db_ceo = crud.get_ceo_by_name(db, ceo_name=ceo_name)
    if db_ceo is None:
        raise HTTPException(status_code=404, detail="CEO not found")
    return db_ceo

@app.post("/ceos", response_model=schemas.CEO)
def create_ceo(ceo: schemas.CEOCreate = Body(...), db: Session = Depends(get_db)):
    return crud.create_ceo(db=db, ceo=ceo)

@app.delete("/ceos/id/{ceo_id}", response_model=schemas.CEO)
def delete_ceo(ceo_id: int, db: Session = Depends(get_db)):
    db_ceo = crud.delete_ceo(db, ceo_id=ceo_id)
    if db_ceo is None:
        raise HTTPException(status_code=404, detail="CEO not found")
    return db_ceo

@app.delete("/ceos/name/{ceo_name}", response_model=schemas.CEO)
def delete_ceo_by_name(ceo_name: str, db: Session = Depends(get_db)):
    db_ceo = crud.delete_ceo_by_name(db, ceo_name=ceo_name)
    if db_ceo is None:
        raise HTTPException(status_code=404, detail="CEO not found")
    return db_ceo

@app.put("/ceos/id/{ceo_id}", response_model=schemas.CEO)
def update_ceo_by_id(ceo_id: int, ceo: schemas.CEOUpdate = Body(...), db: Session = Depends(get_db)):
    db_ceo = crud.update_ceo_by_id(db, ceo_id=ceo_id, ceo=ceo)
    if db_ceo is None:
        raise HTTPException(status_code=404, detail="CEO not found")
    return db_ceo

@app.put("/ceos/name/{ceo_name}", response_model=schemas.CEO)
def update_ceo_by_name(ceo_name: str, ceo: schemas.CEOUpdate = Body(...), db: Session = Depends(get_db)):
    db_ceo = crud.update_ceo_by_name(db, ceo_name=ceo_name, ceo=ceo)
    if db_ceo is None:
        raise HTTPException(status_code=404, detail="CEO not found")
    return db_ceo

@app.patch("/ceos/id/{ceo_id}", response_model=schemas.CEO)
def patch_ceo_by_id(ceo_id: int, ceo: schemas.CEOPatch = Body(...), db: Session = Depends(get_db)):
    db_ceo = crud.patch_ceo_by_id(db, ceo_id=ceo_id, ceo=ceo)
    if db_ceo is None:
        raise HTTPException(status_code=404, detail="CEO not found")
    return db_ceo

@app.patch("/ceos/name/{ceo_name}", response_model=schemas.CEO)
def patch_ceo_by_name(ceo_name: str, ceo: schemas.CEOPatch = Body(...), db: Session = Depends(get_db)):
    db_ceo = crud.patch_ceo_by_name(db, ceo_name=ceo_name, ceo=ceo)
    if db_ceo is None:
        raise HTTPException(status_code=404, detail="CEO not found")
    return db_ceo

from fastapi import FastAPI, Depends, HTTPException, Body, status
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
    return {"message": "Welcome to the CEO API"}

@app.get("/ceos/id/{ceo_id}", response_model=schemas.CEO)
def read_ceo_by_id(ceo_id: int, db: Session = Depends(get_db)):
    db_ceo = crud.get_ceo_by_id(db, ceo_id=ceo_id)
    if db_ceo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"CEO with ID {ceo_id} not found"
        )
    return {"message": "CEO retrieved successfully", "data": db_ceo}

@app.post("/ceos", response_model=schemas.CEO)
def create_ceo(ceo: schemas.CEOCreate = Body(...), db: Session = Depends(get_db)):
    try:
        db_ceo = crud.create_ceo(db=db, ceo=ceo)
        return {"message": "CEO created successfully", "data": db_ceo}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Error creating CEO: {e}"
        )

@app.delete("/ceos/id/{ceo_id}", response_model=schemas.CEO)
def delete_ceo(ceo_id: int, db: Session = Depends(get_db)):
    db_ceo = crud.get_ceo_by_id(db, ceo_id=ceo_id)
    if db_ceo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"CEO with ID {ceo_id} not found"
        )
    try:
        crud.delete_ceo(db, ceo_id=ceo_id)
        return {"message": "CEO deleted successfully", "data": db_ceo}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Error deleting CEO: {e}"
        )

@app.put("/ceos/id/{ceo_id}", response_model=schemas.CEO)
def update_ceo_by_id(ceo_id: int, ceo: schemas.CEOUpdate = Body(...), db: Session = Depends(get_db)):
    db_ceo = crud.get_ceo_by_id(db, ceo_id=ceo_id)
    if db_ceo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"CEO with ID {ceo_id} not found"
        )
    try:
        updated_ceo = crud.update_ceo_by_id(db, ceo_id=ceo_id, ceo=ceo)
        return {"message": "CEO updated successfully", "data": updated_ceo}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Error updating CEO: {e}"
        )

@app.patch("/ceos/id/{ceo_id}", response_model=schemas.CEO)
def patch_ceo_by_id(ceo_id: int, ceo: schemas.CEOPatch = Body(...), db: Session = Depends(get_db)):
    db_ceo = crud.get_ceo_by_id(db, ceo_id=ceo_id)
    if db_ceo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"CEO with ID {ceo_id} not found"
        )
    try:
        patched_ceo = crud.patch_ceo_by_id(db, ceo_id=ceo_id, ceo=ceo)
        return {"message": "CEO patched successfully", "data": patched_ceo}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Error patching CEO: {e}"
        )

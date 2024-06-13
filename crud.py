from sqlalchemy.orm import Session
import models
import schemas

def get_ceo_by_id(db: Session, ceo_id: int):
    return db.query(models.CEO).filter(models.CEO.id == ceo_id).first()

def get_ceo_by_name(db: Session, ceo_name: str):
    return db.query(models.CEO).filter(models.CEO.name == ceo_name).first()

def create_ceo(db: Session, ceo: schemas.CEOCreate):
    db_ceo = models.CEO(**ceo.dict())
    db.add(db_ceo)
    db.commit()
    db.refresh(db_ceo)
    return db_ceo

from sqlalchemy.orm import Session
import models
import schemas

def get_ceo_by_id(db: Session, ceo_id: int):
    return db.query(models.CEO).filter(models.CEO.id == ceo_id).first()



def create_ceo(db: Session, ceo: schemas.CEOCreate):
    db_ceo = models.CEO(**ceo.dict())
    db.add(db_ceo)
    db.commit()
    db.refresh(db_ceo)
    return db_ceo

def delete_ceo(db: Session, ceo_id: int):
    db_ceo = db.query(models.CEO).filter(models.CEO.id == ceo_id).first()
    if db_ceo is None:
        return None
    db.delete(db_ceo)
    db.commit()
    return db_ceo



def update_ceo_by_id(db: Session, ceo_id: int, ceo: schemas.CEOUpdate):
    db_ceo = db.query(models.CEO).filter(models.CEO.id == ceo_id).first()
    if db_ceo is None:
        return None
    for key, value in ceo.dict().items():
        setattr(db_ceo, key, value)
    db.commit()
    db.refresh(db_ceo)
    return db_ceo



def patch_ceo_by_id(db: Session, ceo_id: int, ceo: schemas.CEOPatch):
    db_ceo = db.query(models.CEO).filter(models.CEO.id == ceo_id).first()
    if db_ceo is None:
        return None
    for key, value in ceo.dict(exclude_unset=True).items():
        setattr(db_ceo, key, value)
    db.commit()
    db.refresh(db_ceo)
    return db_ceo


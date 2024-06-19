from sqlalchemy.orm import Session
import models
import schemas

def get_ceo_by_id(db: Session, ceo_id: int):
    try:
        ceo = db.query(models.CEO).filter(models.CEO.id == ceo_id).first()
        if not ceo:
            raise ValueError(f"CEO with ID {ceo_id} does not exist")
        return ceo
    except Exception as e:
        raise ValueError(f"An error occurred while retrieving CEO by ID: {e}")

def create_ceo(db: Session, ceo: schemas.CEOCreate):
    try:
        db_ceo = models.CEO(**ceo.dict())
        db.add(db_ceo)
        db.commit()
        db.refresh(db_ceo)
        return db_ceo
    except Exception as e:
        raise ValueError(f"An error occurred while creating CEO: {e}")

def delete_ceo(db: Session, ceo_id: int):
    try:
        ceo = db.query(models.CEO).filter(models.CEO.id == ceo_id).first()
        if not ceo:
            raise ValueError(f"CEO with ID {ceo_id} does not exist")
        db.delete(ceo)
        db.commit()
        return ceo
    except Exception as e:
        raise ValueError(f"An error occurred while deleting CEO: {e}")

def update_ceo_by_id(db: Session, ceo_id: int, ceo: schemas.CEOUpdate):
    try:
        db_ceo = db.query(models.CEO).filter(models.CEO.id == ceo_id).first()
        if not db_ceo:
            raise ValueError(f"CEO with ID {ceo_id} does not exist")
        for key, value in ceo.dict().items():
            setattr(db_ceo, key, value)
        db.commit()
        db.refresh(db_ceo)
        return db_ceo
    except Exception as e:
        raise ValueError(f"An error occurred while updating CEO: {e}")

def patch_ceo_by_id(db: Session, ceo_id: int, ceo: schemas.CEOPatch):
    try:
        db_ceo = db.query(models.CEO).filter(models.CEO.id == ceo_id).first()
        if not db_ceo:
            raise ValueError(f"CEO with ID {ceo_id} does not exist")
        for key, value in ceo.dict(exclude_unset=True).items():
            setattr(db_ceo, key, value)
        db.commit()
        db.refresh(db_ceo)
        return db_ceo
    except Exception as e:
        raise ValueError(f"An error occurred while patching CEO: {e}")

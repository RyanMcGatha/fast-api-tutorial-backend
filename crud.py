from sqlalchemy.orm import Session
import models
import schemas

def get_ceo(db: Session, ceo_id: int):
    return db.query(models.CEO).filter(models.CEO.id == ceo_id).first()

def create_ceo(db: Session, ceo: schemas.CEOCreate):
    db_ceo = models.CEO(name=ceo.name, company=ceo.company)
    db.add(db_ceo)
    db.commit()
    db.refresh(db_ceo)
    return db_ceo

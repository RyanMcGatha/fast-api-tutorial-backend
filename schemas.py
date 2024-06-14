from pydantic import BaseModel
from typing import Optional

class CEOBase(BaseModel):
    name: str
    company: str

class CEOCreate(CEOBase):
    pass

class CEOUpdate(CEOBase):
    pass

class CEOPatch(BaseModel):
    name: Optional[str] = None
    company: Optional[str] = None

class CEO(CEOBase):
    id: int

    class Config:
        orm_mode = True

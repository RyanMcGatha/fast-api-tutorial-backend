from pydantic import BaseModel

class CEOBase(BaseModel):
    name: str
    company: str

class CEOCreate(CEOBase):
    pass

class CEO(CEOBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel

class CEOBase(BaseModel):
    name: str
    age: int
    company: str

class CEOCreate(CEOBase):
    pass

class CEOUpdate(CEOBase):
    pass

class CEO(CEOBase):
    id: int

    class Config:
        orm_mode = True

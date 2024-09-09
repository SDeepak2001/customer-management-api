from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True

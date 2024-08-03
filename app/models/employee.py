from sqlalchemy import Column, Integer, String
from ..database import Base
from pydantic import BaseModel

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

class EmployeeCreate(BaseModel):
    name: str
    email: str
    phone: str

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str

    class Config:
        from_attributes = True  # This replaces orm_mode
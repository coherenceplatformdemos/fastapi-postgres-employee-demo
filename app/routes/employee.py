from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import SQLAlchemyError
import logging

from ..database import get_db
from ..models.employee import Employee, EmployeeCreate, EmployeeResponse

router = APIRouter()

@router.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        db_employee = Employee(**employee.dict())
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except SQLAlchemyError as e:
        db.rollback()
        logging.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.get("/employees/", response_model=List[EmployeeResponse])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        employees = db.query(Employee).offset(skip).limit(limit).all()
        logging.info(f"Employees retrieved: {employees}")
        return employees
    except SQLAlchemyError as e:
        logging.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.get("/employees/{employee_id}", response_model=EmployeeResponse)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if db_employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return db_employee
    except SQLAlchemyError as e:
        logging.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if db_employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        for key, value in employee.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except SQLAlchemyError as e:
        db.rollback()
        logging.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.delete("/employees/{employee_id}", response_model=EmployeeResponse)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if db_employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        db.delete(db_employee)
        db.commit()
        return db_employee
    except SQLAlchemyError as e:
        db.rollback()
        logging.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.get("/debug/employees/")
def debug_employees(db: Session = Depends(get_db)):
    try:
        employees = db.query(Employee).all()
        return {
            "count": len(employees),
            "employees": [{"id": e.id, "name": e.name, "email": e.email, "phone": e.phone} for e in employees]
        }
    except SQLAlchemyError as e:
        logging.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
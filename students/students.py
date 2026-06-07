from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schemas import (
    StudentCreate,
    StudentUpdate,
    StudentPatch,
    StudentResponse
)

router = APIRouter(tags=["Students"])


students_data = [
    {"id": 1, "name": "Omkar", "age": 21, "course": "AI"},
    {"id": 2, "name": "Rahul", "age": 22, "course": "Data Science"},
    {"id": 3, "name": "Priya", "age": 20, "course": "Machine Learning"},
    {"id": 4, "name": "Amit", "age": 23, "course": "Python"},
    {"id": 5, "name": "Sneha", "age": 19, "course": "Cyber Security"}
]


@router.post("/seed")
def seed_data(db: Session = Depends(get_db)):
    inserted = 0

    for item in students_data:
        existing = db.query(Student).filter(
            Student.id == item["id"]
        ).first()

        if not existing:
            db.add(Student(**item))
            inserted += 1

    db.commit()

    return {"message": f"{inserted} records inserted"}


@router.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(Student).filter(
        Student.id == student.id
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Student already exists"
        )

    new_student = Student(**student.model_dump())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@router.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):
    return db.query(Student).all()


@router.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db_student.name = student.name
    db_student.age = student.age
    db_student.course = student.course

    db.commit()
    db.refresh(db_student)

    return db_student


@router.patch(
    "/students/{student_id}",
    response_model=StudentResponse
)
def patch_student(
    student_id: int,
    student: StudentPatch,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_data = student.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(db_student, field, value)

    db.commit()
    db.refresh(db_student)

    return db_student


@router.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(db_student)
    db.commit()

    return {
        "message": f"Student {student_id} deleted"
    }
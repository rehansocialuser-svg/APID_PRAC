from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentModel(BaseModel):
    name: str
    age: int

students_db = []

@app.post("/students")
def create_student(student_data: StudentModel):
    students_db.append(student_data.dict())
    return {
        "msg": "student created successfully",
        "student": student_data
    }

@app.get("/student-data")
def get_all_students():
    return students_db
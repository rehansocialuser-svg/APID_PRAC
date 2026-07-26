from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Nested Model
class Address(BaseModel):
    city: str
    state: str
    pincode: int

# Parent Model
class Student(BaseModel):
    name: str
    age: int
    email: str
    address: Address

# POST API
@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student Added Successfully",
        "student": student
    }

# GET API
@app.get("/")
def home():
    return {"message": "Nested Model API"}
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

students = {
    1: "Nitish",
    2: "Rahul"
}

# Custom Exception
class StudentNotFound(Exception):

    def __init__(self, student_id):
        self.student_id = student_id

# Exception Handler
@app.exception_handler(StudentNotFound)

async def student_not_found_handler(request: Request,
                                    exc: StudentNotFound):

    return JSONResponse(
        status_code=404,
        content={
            "message": f"Student {exc.student_id} Not Found"
        }
    )

# API
@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise StudentNotFound(student_id)

    return {
        "id": student_id,
        "name": students[student_id]
    }
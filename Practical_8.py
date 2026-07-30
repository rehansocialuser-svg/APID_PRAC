from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class Library(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        description="Library name must be between 3 and 50 characters."
    )

    location: str = Field(
        min_length=3,
        max_length=100,
        description="Location name must be between 3 and 100 characters."
    )

    librarian_email: EmailStr = Field(
        description="Valid email address of the librarian."
    )

    total_books: int = Field(
        gt=0,
        lt=100000,
        description="Total number of books must be between 1 and 100000."
    )

    membership_fee: float = Field(
        gt=0,
        description="Membership fee must be a positive value."
    )

@app.post("/library/")
def create_library(library: Library):
    return {"message": "Library record created successfully!", "data": library}

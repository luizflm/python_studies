from fastapi import FastAPI
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
    },
    2: {
        "name": "Jane",
        "age": 16,
    },
}


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/students/name")
def get_student(name: Optional[str] = None):
    for student in students:
        if students[student]["name"] == name:
            return students[student]
    return {"data": "Not Found"}


@app.get("/students/{student}")
def get_student(student: int):
    return students[student]

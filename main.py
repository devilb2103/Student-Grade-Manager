from fastapi import FastAPI
from pydantic import BaseModel
from Controller.auth_controller import *
from Controller.student_controller import *

app = FastAPI()

class auth_data(BaseModel):
    user: str
    pswd: str

# base route
@app.get("/")
async def up_state():
    return "server is up and running"

@app.post("/login")
async def login(body: auth_data):
    access = await VerifyRequest(body.user, body.pswd)
    return access

# get all students route
@app.get("/get/students")
async def get_students():
    return await GetStudents()

# add student route
class add_student_request_body(BaseModel):
    name: str = ""
    grades: list = []

@app.post("/create/students")
async def add_student(body: add_student_request_body):
    return await AddStudent(body.name, body.grades)

# update student marks route
class modify_student_request_body(BaseModel):
    id: int
    grades: list
@app.put("/update/grades")
async def change_student(body: modify_student_request_body):
    return await UpdateMarks(body.id, body.grades)

# delete student route
class delete_student_request_body(BaseModel):
    id: int
@app.delete("/delete/student")
async def delete_student(body: delete_student_request_body):
    return await DeleteStudent(body.id)
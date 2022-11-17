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

@app.get("/login")
async def login(body: auth_data):
    access = await VerifyRequest(body.user, body.pswd)
    return access

# get all students route
@app.get("/get/students")
async def get_students(body: auth_data):
    access = await VerifyRequest(body.user, body.pswd)
    if(access["status"] == 401):
        return access
    return await GetStudents()

# add student route
class student_request_body(BaseModel):
    auth: auth_data
    name: str = ""
    grades: list = []

@app.post("/create/students")
async def add_student(body: student_request_body):
    access = await VerifyRequest(body.auth.user, body.auth.pswd)
    if(access["status"] == 401):
        return access
    return await AddStudent(body.name, body.grades)
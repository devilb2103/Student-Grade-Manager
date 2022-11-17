from Models.student_model import *

student_details = {1:student(name="Dev", grades=[1,2,3,4])}

async def GetStudents():
    try:
        return {
            "status" : 200,
            "message" : student_details
            }
    except Exception as e:
        return {
            "status" : 400,
            "message" : e
        }

async def AddStudent(name, grades):
    try:
        id = len(list(student_details.keys())) + 1
        new_student = student(name=name, grades=grades)
        student_details[id] = new_student
        return {
            "status" : 200,
            "message" : f"student with id {id} added successfully",
            "data" : {id: new_student}
            }
    except Exception as e:
        print(e)
        return {
            "status" : 400,
            "message" : e
        }
from Models.student_model import *

student_details = {1:student(name="Dev", grades=(1,2,3,4))}

async def GetStudents():
    try:
        return {
            "status" : 200,
            "message" : student_details
            }
    except Exception as e:
        return {
            "status" : 400,
            "message" : str(e)
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
        return {
            "status" : 400,
            "message" : str(e)
        }

async def UpdateMarks(id, grades):
    if(id in list(student_details)):
        try:
            student_details[id].grades = grades
            return {
            "status" : 200,
            "message" : f"marks of student with id {id} updated to successfully",
            "data" : student_details[id]
            }
        except Exception as e:
            return {
                "status" : 400,
                "message" : str(e)
            }
    else:
        return {
        "status" : 400,
        "message" : f"student with id {id} does not exist"
    }

async def DeleteStudent(id):
    if(id in list(student_details)):
        try:
            student = student_details[id]
            del student_details[id]
            return {
            "status" : 200,
            "message" : f"student with id {id} deleted successfully",
            "data" : student
            }
        except Exception as e:
            return {
                "status" : 400,
                "message" : str(e)
            }
    else:
        return {
        "status" : 400,
        "message" : f"student with id {id} does not exist"
    }
from pydantic import BaseModel

class student(BaseModel):
    name: str
    grades: list
    average: int = 0
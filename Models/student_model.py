from ctypes import Union

class student():
    def __init__(self, name, grades):
        self.name = name
        # self.year = year
        # self.branch = branch
        self.grades = grades
    
    def __repr__(self) -> dict:
        {
            "name" : self.name,
            # "year" : self.year,
            # "branch" : self.branch,
            "grades": self.grades
        }
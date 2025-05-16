
from CSE_324_course import Course


class Student:
    
    student_id = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + self.last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1
    
        
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return self.full_name
        
    def get_student_id(self):
        return self.student_id
    
    

        
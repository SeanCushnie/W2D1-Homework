# Student_Sean = Student('Sean', 'G37')

class Student:
    def __init__(self, student_name, Cohort_Name):
        self.name = student_name
        self.cohort = Cohort_Name


    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, language):
        return "I love " + language
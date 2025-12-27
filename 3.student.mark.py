import numpy as np
import math

class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""
        self.__mark = {}    #{courseID:mark}

    def input(self):
        self.__id = input("Student ID: ")
        self.__name = input("Student Name: ")
        self.__dob = input("Student DOB: ")
        print("----------")

    def getID(self): 
        return self.__id 

    def getName(self):
        return self.__name
    
    def getDob(self):
        return self.__dob
    
    def getMark(self):
        return self.__mark

    def addMark(self, courseID, mark):
        self.__mark[courseID] = math.floor(mark)


class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__credits = 0
    
    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")
        self.__credits = int(input("Course Credit:"))
        print("----------")

    def getID(self): 
        return self.__id 

    def getName(self):
        return self.__name
    
    def getCredit(self):
        return self.__credits
    
def getGPA(student, course_db):
    #student: student object
    #course_db: a dict {course_id:course object}

    studied_course_id = list(student.getMark().keys())
    scores = list(student.getMark().values())

    credits = []

    for cid in studied_course_id:
        if cid in course_db:
            course_obj = course_db[cid]
            credits.append(course_obj.getCredit())
    
    np_mark = np.array(scores)
    np_credit = np.array(credits)

    gpa = np.average(np_mark,weights=np_credit)
    return gpa


classroom = []      #student list 
course_database = {}    #course list
studentNum = int(input("#students: "))
courseNum = int(input("#courses: "))

print("----------Enter student details---------- ")
for i in range(studentNum):
    s = Student()
    s.input()
    classroom.append(s)

print("----------Enter course details---------- ")
for j in range(courseNum):
    c = Course()
    c.input()
    course_database[c.getID()] = c

print("----------Course List----------")
for c in course_database.values():
    print(f"Course name: {c.getName()} - Course ID: {c.getID()}")

while True:
    selected_course_id = input("Enter the ID of course that you want to add mark (Type 'exit' to stop): ")
    if selected_course_id == "exit": 
        break 
    else:
        for s in classroom:
            print(f"Student: {s.getName()} - ID: {s.getID()}")
            mark = int(input("Enter the mark: "))
            s.addMark(selected_course_id, mark)

print("----------GPA----------")
for s in classroom:
    print(f"Studednt: {s.getName()} - GPA: {getGPA(s,course_database)}")
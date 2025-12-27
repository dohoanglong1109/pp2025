import math
import numpy as np

class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""
        self.__mark = {}    #{courseID:mark}
        self.__gpa = 0

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

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, value):
        self.__gpa = value

    def addMark(self, courseID, mark):
        self.__mark[courseID] = math.floor(mark)

    def calculate_gpa(self, course_db): #list, dict {course_id:object Course}
        studied_course_mark = list(self.getMark().values())
        studies_course_id = list(self.getMark().keys())

        credits = []
        for cid in studies_course_id:
            if cid in course_db:
                course_obj = course_db[cid]
                credits.append(course_obj.getCredits())
            else:
                credits.append(0)

        mark_np = np.array(studied_course_mark)
        credit_np = np.array(credits)
        if np.sum(credit_np) == 0:
            return 0.0

        gpa = np.average(mark_np, weights=credit_np)

        return gpa
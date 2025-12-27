class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""
        self.__mark = {}    #{subject:mark}

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

    def addMark(self, courseID, mark):
        self.__mark[courseID] = mark


class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""
    
    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")
        print("----------")

    def getID(self): 
        return self.__id 

    def getName(self):
        return self.__name
    


classroom = []      #student list 
course_list = []    #course list
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
    course_list.append(c)

print("----------Course List----------")
for c in course_list:
    print(f"Course name: {c.getName()} - Course ID: {c.getID()}")

while True:
    selected_course_id = input("Enter the ID of course that you want to add mark (Type 'exit' to stop): ")
    if selected_course_id == "exit": 
        break 
    else:
        for s in classroom:
            print(f"Student: {s.getName()} - ID: {s.getID()}")
            mark = float(input("Enter the mark: "))
            s.addMark(selected_course_id, mark)


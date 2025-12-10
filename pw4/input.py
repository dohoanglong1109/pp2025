from domains.student import Student
from domains.course import Course

def input_student():
    classroom = []      #student list 
    studentNum = int(input("#students: "))
    print("----------Enter student details---------- ")
    for i in range(studentNum):
        s = Student()
        s.input()
        classroom.append(s)

    return classroom

def input_course():
    course_database = {}    #course list
    courseNum = int(input("#courses: "))
    print("----------Enter course details---------- ")
    for j in range(courseNum):
        c = Course()
        c.input()
        course_database[c.getID()] = c
    
    return course_database

def input_mark(classroom, course_db):
    while True:
        selected_course_id = input("Enter the ID of course that you want to add mark (Type 'exit' to stop): ")
        
        if selected_course_id == "exit": 
            break
        #Course available check
        if selected_course_id not in course_db:
            print(f"Error: Course ID '{selected_course_id}' does not exit! Try again.")
            continue

         
        else:
            for s in classroom:
                print(f"Student: {s.getName()} - ID: {s.getID()}")
                mark = int(input("Enter the mark: "))
                s.addMark(selected_course_id, mark)
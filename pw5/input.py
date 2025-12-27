from domains.student import Student
from domains.course import Course
import csv
import json 

def save_to_csv(classroom):
    with open('student.csv', 'w', newline="", encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow(["ID", "Name", "DoB", "GPA"])

        for s in classroom:
            writer.writerow([s.getID(), s.getName(), s.getDob(), s.getGPA()])

def save_to_json(classroom):
    report = []
    for s in classroom:
        report.append({
            "id": s.getID(),
            "name": s.getName(),
            "marks": s.getMark(),
            "gpa": s.getGPA()
        })
    
    with open('report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)


def input_student():
    classroom = []      #student list 
    studentNum = int(input("#students: "))
    print("----------Enter student details---------- ")
    for i in range(studentNum):
        s = Student()
        s.input()
        classroom.append(s)

    save_to_csv(classroom)

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
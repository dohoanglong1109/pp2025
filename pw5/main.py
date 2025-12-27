import input
import output

def main():
    classroom = input.input_student()
    course_db = input.input_course()
    input.input_mark(classroom, course_db) 

    for s in classroom:
        s.set_gpa(s.calGPA(course_db))

    input.save_students_csv(classroom)
    input.save_courses_csv(course_db)
    input.save_report_json(classroom)

    output.print_student_list(classroom)

if __name__ == "__main__":
    main()
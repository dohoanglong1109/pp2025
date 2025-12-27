import input
import output

def main():
    classroom = input.input_student()
    course_db = input.input_course()
    input.input_mark(classroom, course_db) 

    for s in classroom:
        s.set_gpa(s.calGPA(course_db))

    input.save_student_to_csv(classroom)
    input.save_course_to_csv(course_db)
    input.save_mark_to_json(classroom)
    
    output.print_student_list(classroom)

if __name__ == "__main__":
    main()
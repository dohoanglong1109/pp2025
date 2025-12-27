import input
import output

def main():
    classroom = input.input_student()
    course_db = input.input_course()
    input.input_mark(classroom, course_db) 

    for s in classroom:
        s.set_gpa(s.calculate_gpa(course_db))

    output.print_student_list(classroom)

if __name__ == "__main__":
    main()
import input
import output

def main():
    classroom = input.input_student()
    course_db = input.input_course()
    input.input_mark(classroom, course_db) 

    for s in classroom:
        # Gọi hàm tính GPA ở đây (hoặc hàm getGPA nằm trong domains)
        # Giả sử bạn gán tạm vào thuộc tính .gpa để output dễ lấy
        s.getGpa = s.calculate_gpa(course_db) # Bạn cần viết hàm này trong class Student nhé

    output.print_student_list(classroom)

if __name__ == "__main__":
    main()
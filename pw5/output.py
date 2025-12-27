import curses

def draw_results(stdscr, students):
    """
    Hàm này thực hiện việc vẽ lên màn hình.
    stdscr: là cái màn hình (window object) do curses tự tạo.
    students: list sinh viên được truyền vào.
    """
    
    # 1. Xóa sạch màn hình trước khi vẽ
    stdscr.clear()

    # 2. Vẽ tiêu đề (Dòng 0, Cột 0)
    # addstr(y, x, string, [attr])
    stdscr.addstr(0, 0, "RESULT BOARD", curses.A_BOLD)
    stdscr.addstr(1, 0, "=" * 50) # Vẽ đường kẻ ngang

    # 3. Vẽ tiêu đề cột (Dòng 2)
    stdscr.addstr(2, 0, "ID")
    stdscr.addstr(2, 10, "Full Name")        # Cách lề trái 10 ký tự
    stdscr.addstr(2, 30, "DOB")     # Cách lề trái 30 ký tự
    stdscr.addstr(2, 50, "GPA")           # Cách lề trái 50 ký tự

    # 4. Duyệt list và vẽ từng sinh viên
    row = 3 # Bắt đầu vẽ từ dòng thứ 3
    for s in students:
        # Lấy thông tin
        # Lưu ý: s.getID() phải trả về string, gpa phải ép về string
        stdscr.addstr(row, 0,  str(s.getID()))
        stdscr.addstr(row, 10, str(s.getName()))
        stdscr.addstr(row, 30, str(s.getDob()))
        
        # Tính GPA (Giả sử bạn đã có hàm getGPA hoặc thuộc tính gpa)
        # Nếu chưa tính thì gọi hàm tính ở đây, hoặc lấy giá trị đã lưu
        # Ví dụ này mình giả định bạn đã tính và lưu vào s.gpa (hoặc gọi hàm)
        # Bạn có thể gọi hàm getGPA(s, db) ở main rồi lưu vào s trước khi truyền vào đây
        gpa_val = "N/A" # Placeholder nếu chưa tính
        
        # Giả sử bạn sửa class Student có thêm thuộc tính gpa sau khi tính
        if hasattr(s, 'gpa'): 
            gpa_val = f"{s.getGPA():.2f}"
            
        stdscr.addstr(row, 50, gpa_val)
        
        row += 1 # Xuống dòng cho sinh viên tiếp theo

    # 5. Thông báo chân trang
    stdscr.addstr(row + 1, 0, "Press any button to exit...", curses.A_BLINK)

    # 6. Quan trọng: Refresh màn hình để hiện những gì đã vẽ
    stdscr.refresh()

    # 7. Chờ người dùng bấm phím bất kỳ mới thoát
    stdscr.getch()

# Hàm wrapper bên ngoài để main.py gọi
def print_student_list(students):
    # wrapper sẽ tự khởi tạo stdscr và truyền nó vào hàm draw_results
    # tham số students sẽ được truyền tiếp theo sau
    curses.wrapper(draw_results, students)

def input_number_students():
    """Input number of students in a class"""
    n = int(input("Number of students: "))
    return n

def input_student_info():
    """Input student information: id, name, DoB"""
    student_id = input("Student id: ")
    name = input("Name: ")
    dob = input("Date of birth: ")
    
    return (student_id, name, dob)

def input_number_courses():
    """Input number of courses"""
    n = int(input("Number of courses: "))
    return n

def input_course_info():
    """Input course information: id, name"""
    course_id = input("Course id: ")
    name = input("Course name: ")
    return (course_id, name)

def select_course(courses):
    """Select a course from the list"""
    print("\nAvailable courses:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course[1]} ({course[0]})")
    
    while True:
        try:
            choice = int(input("Select a course (enter number): "))
            if 1 <= choice <= len(courses):
                return courses[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def input_marks_for_course(course, students, marks):
    """Select a course, input marks for students in this course"""
    course_id = course[0]
    course_name = course[1]
    
    print(f"\nEntering marks for course: {course_name}")
    
    # Initialize marks dict for this course if not exists
    if course_id not in marks:
        marks[course_id] = {}
    
    for student in students:
        student_id = student[0]
        student_name = student[1]
        mark = float(input(f"Mark for {student_name} ({student_id}): "))
        marks[course_id][student_id] = mark



def list_courses(courses):
    """List courses"""
    print("\nCourse list:")
    if not courses:
        print("No courses available.")
    else:
        for course in courses:
            print(f"  - {course[1]} (ID: {course[0]})")

def list_students(students):
    """List students"""
    print("\nStudent list:")
    if not students:
        print("No students available.")
    else:
        for student in students:
            print(f"  - {student[1]} (ID: {student[0]}, DoB: {student[2]})")

def show_student_marks_for_course(course, students, marks):
    """Show student marks for a given course"""
    course_id = course[0]
    course_name = course[1]
    
    print(f"\nStudent marks for course: {course_name}")
    
    if course_id not in marks or not marks[course_id]:
        print("No marks available for this course.")
        return
    
    for student in students:
        student_id = student[0]
        student_name = student[1]
        
        if student_id in marks[course_id]:
            mark = marks[course_id][student_id]
            print(f"  - {student_name} ({student_id}): {mark}")
        else:
            print(f"  - {student_name} ({student_id}): No mark")




students = []
courses = []
marks = {}  


print("=" * 50)
print("STUDENT MARK MANAGEMENT SYSTEM")
print("=" * 50)


print("\n--- Input Students ---")
n_students = input_number_students()
for i in range(n_students):
    print(f"\nEnter student info {i + 1}:")
    s = input_student_info()
    students.append(s)


print("\n--- Input Courses ---")
n_courses = input_number_courses()
for i in range(n_courses):
    print(f"\nEnter course info {i + 1}:")
    c = input_course_info()
    courses.append(c)
    marks[c[0]] = {}  


print("\n--- Input Marks ---")
if courses:
    while True:
        selected_course = select_course(courses)
        input_marks_for_course(selected_course, students, marks)
        
        continue_input = input("\nDo you want to input marks for another course? (y/n): ")
        if continue_input.lower() != 'y':
            break
else:
    print("No courses available. Cannot input marks.")


print("\n" + "=" * 50)
print("OUTPUT")
print("=" * 50)


list_courses(courses)


list_students(students)


if courses:
    print("\n--- Marks ---")
    for course in courses:
        show_student_marks_for_course(course, students, marks)

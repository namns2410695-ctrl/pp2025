

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
    
    # Encapsulation: getters
    def get_student_id(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    @staticmethod
    def input():
        student_id = input("Student id: ")
        name = input("Name: ")
        dob = input("Date of birth: ")
        return Student(student_id, name, dob)
    
    def list(self):
        return (self.__student_id, self.__name, self.__dob)
    
    def __str__(self):
        return str(self.list())


class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name
    
    # Encapsulation: getters
    def get_course_id(self):
        return self.__course_id
    
    def get_name(self):
        return self.__name
    
    # Polymorphism: input method
    @staticmethod
    def input():
        course_id = input("Course id: ")
        name = input("Course name: ")
        return Course(course_id, name)
    
    # Polymorphism: list method
    def list(self):
        return (self.__course_id, self.__name)
    
    def __str__(self):
        return str(self.list())


class Mark:
    def __init__(self, course_id, student_id, mark):
        self.__course_id = course_id
        self.__student_id = student_id
        self.__mark = mark
    
    # Encapsulation: getters
    def get_course_id(self):
        return self.__course_id
    
    def get_student_id(self):
        return self.__student_id
    
    def get_mark(self):
        return self.__mark
    
    # Encapsulation: setter
    def set_mark(self, mark):
        self.__mark = mark


class StudentMarkManager:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # key is course id, value is dict of student id to Mark object
    
    # Encapsulation: getters
    def get_students(self):
        return self.__students
    
    def get_courses(self):
        return self.__courses
    
    def get_marks(self):
        return self.__marks
    
    # Input methods
    def input_number_students(self):
        n = int(input("Number of students: "))
        return n
    
    def input_number_courses(self):
        n = int(input("Number of courses: "))
        return n
    
    def input_student_info(self):
        return Student.input()
    
    def input_course_info(self):
        return Course.input()
    
    def input_mark(self, student):
        m = float(input(f"Mark for {student.get_name()} ({student.get_student_id()}): "))
        return m
    
    def select_course(self):
        """Select a course from the list"""
        if not self.__courses:
            return None
        
        print("\nAvailable courses:")
        for i, course in enumerate(self.__courses, 1):
            print(f"{i}. {course.get_name()} ({course.get_course_id()})")
        
        while True:
            try:
                choice = int(input("Select a course (enter number): "))
                if 1 <= choice <= len(self.__courses):
                    return self.__courses[choice - 1]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    # Main input section
    def input_students(self):
        n_students = self.input_number_students()
        for i in range(n_students):
            print(f"\nEnter student info {i + 1}:")
            s = self.input_student_info()
            self.__students.append(s)
    
    def input_courses(self):
        n_courses = self.input_number_courses()
        for i in range(n_courses):
            print(f"\nEnter course info {i + 1}:")
            c = self.input_course_info()
            self.__courses.append(c)
            self.__marks[c.get_course_id()] = {}  # create empty mark dict for this course
    
    def input_marks_for_course(self, course):
        """Select a course, input marks for students in this course"""
        course_id = course.get_course_id()
        course_name = course.get_name()
        
        print(f"\nEntering marks for course: {course_name}")
        
        # Initialize marks dict for this course if not exists
        if course_id not in self.__marks:
            self.__marks[course_id] = {}
        
        for student in self.__students:
            m = self.input_mark(student)
            mark_obj = Mark(course_id, student.get_student_id(), m)
            self.__marks[course_id][student.get_student_id()] = mark_obj
    
    def input_marks(self):
        """Select a course and input marks"""
        if not self.__courses:
            print("No courses available. Cannot input marks.")
            return
        
        while True:
            selected_course = self.select_course()
            if selected_course:
                self.input_marks_for_course(selected_course)
            
            continue_input = input("\nDo you want to input marks for another course? (y/n): ")
            if continue_input.lower() != 'y':
                break
    
    # Output section
    def list_students(self):
        """List students"""
        print("\nStudent list:")
        if not self.__students:
            print("No students available.")
        else:
            for s in self.__students:
                info = s.list()
                print(f"  - {info[1]} (ID: {info[0]}, DoB: {info[2]})")
    
    def list_courses(self):
        """List courses"""
        print("\nCourse list:")
        if not self.__courses:
            print("No courses available.")
        else:
            for c in self.__courses:
                info = c.list()
                print(f"  - {info[1]} (ID: {info[0]})")
    
    def show_student_marks_for_course(self, course):
        """Show student marks for a given course"""
        course_id = course.get_course_id()
        course_name = course.get_name()
        
        print(f"\nStudent marks for course: {course_name}")
        
        if course_id not in self.__marks or not self.__marks[course_id]:
            print("No marks available for this course.")
            return
        
        for s in self.__students:
            sid = s.get_student_id()
            sname = s.get_name()
            
            if sid in self.__marks[course_id]:
                mark_obj = self.__marks[course_id][sid]
                print(f"  - {sname} ({sid}): {mark_obj.get_mark()}")
            else:
                print(f"  - {sname} ({sid}): No mark")
    
    def list_marks(self):
        """Show student marks for all courses"""
        if not self.__courses:
            return
        
        print("\n--- Marks ---")
        for course in self.__courses:
            self.show_student_marks_for_course(course)


# Main program
if __name__ == "__main__":
    manager = StudentMarkManager()
    
    # Input section
    print("=" * 50)
    print("STUDENT MARK MANAGEMENT SYSTEM")
    print("=" * 50)
    
    print("\n--- Input Students ---")
    manager.input_students()
    
    print("\n--- Input Courses ---")
    manager.input_courses()
    
    print("\n--- Input Marks ---")
    manager.input_marks()
    
    # Output section
    print("\n" + "=" * 50)
    print("OUTPUT")
    print("=" * 50)
    
    manager.list_courses()
    manager.list_students()
    manager.list_marks()

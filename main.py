class Student:
    def __init__(self, admission_number, full_name, course, contact_number, marks):
        self.admission_number = admission_number
        self.full_name = full_name
        self.course = course
        self.contact_number = contact_number
        self.marks = marks

    def total_marks(self):
        return sum(self.marks.values())

    def average(self):
        if not self.marks:
            return 0
        return self.total_marks() / len(self.marks)

    def grade(self):
        average = self.average()
        if average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        return "E"

    def result(self):
        return "PASS" if self.average() >= 50 else "FAIL"

    def display_report(self):
        print("\n========== STUDENT REPORT ==========")
        print(f"Admission Number: {self.admission_number}")
        print(f"Full Name: {self.full_name}")
        print(f"Course: {self.course}")
        print(f"Contact: {self.contact_number}")
        print("\nSubject Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print("------------------------------------")
        print(f"Total Marks: {self.total_marks()}")
        print(f"Average: {self.average():.2f}")
        print(f"Grade: {self.grade()}")
        print(f"Result: {self.result()}")
        print("====================================")


students = {}
SUBJECTS = ["Mathematics", "English", "Science"]


def read_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def register_student():
    admission = input("Admission number: ").strip().upper()
    if not admission:
        print("Admission number cannot be empty.")
        return
    if admission in students:
        print("That admission number is already registered.")
        return

    name = input("Full name: ").strip()
    course = input("Course: ").strip()
    contact = input("Contact number: ").strip()
    if not name or not course or not contact:
        print("Name, course and contact number are required.")
        return

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = read_mark(subject)

    students[admission] = Student(admission, name, course, contact, marks)
    print("Student registered successfully!")


def search_student():
    admission = input("Enter admission number: ").strip().upper()
    student = students.get(admission)
    if student:
        student.display_report()
    else:
        print("Student not found.")


def class_summary():
    if not students:
        print("No students have been registered.")
        return

    averages = [student.average() for student in students.values()]
    top_average = max(averages)
    lowest_average = min(averages)
    print("\n========== CLASS SUMMARY ==========")
    print(f"Registered students: {len(students)}")
    print(f"Class average: {sum(averages) / len(averages):.2f}")
    print(f"Highest average: {top_average:.2f}")
    print(f"Lowest average: {lowest_average:.2f}")
    print("Top-performing student(s):")
    for student in students.values():
        if student.average() == top_average:
            print(f"- {student.full_name} ({student.admission_number})")
    print("===================================")


def main_menu():
    while True:
        print("\n===== STUDENT REGISTRATION & RESULTS MANAGER =====")
        print("1. Register student")
        print("2. Search student and view report")
        print("3. Display class summary")
        print("4. List all students")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            class_summary()
        elif choice == "4":
            if not students:
                print("No students registered.")
            else:
                for student in students.values():
                    print(f"{student.admission_number} - {student.full_name} - {student.course}")
        elif choice == "5":
            print("Thank you for using the Student Results Manager!")
            break
        else:
            print("Invalid option. Choose 1-5.")


if __name__ == "__main__":
    main_menu()

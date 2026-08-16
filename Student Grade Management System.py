# Student Grade Management System
# Create a dictionary where student names are keys and their grades are values.
#Allow users to: Add a new student. Update an existing grade. Retrieve a student's grade. Display all students

students = {}

def add_student():
    name = input("Please enter your name: ")
    grade = input("Please enter your grade: ")
    students[name] = grade
    print("Student entered successfully")

def update_grade():
    name = input("Enter student name: ")
    if name in students:
        grade = input("Please enter your grade: ")
        students[name] = grade
        print("Grade updated.")
    else:
        print("Student not found.")

def get_grade():
    name = input("Enter student name: ")
    print(f"{name}'s grade: {students.get(name, 'Not found')}")

def display_all():
    for name, grade in student.items():
        print(f"{name}: {grade}")

while True:
    print("\n1: Add Student\n2. Update Grade\n3. Get Grade\n4. Display All\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        get_grade()
    elif choice == "4":
        display_all()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")

from datetime import datetime
from logging import raiseExceptions

def menu():
        print("Choose an option:")
        print("1. Import students from file")
        print("2. Add a new student")
        print("3. Mark student attendance")
        print("4. Edit student attendance")
        print("5. Remove a student from the database")
        print("6. Save the student list to a file")
        print("7. Exit")
        option = input("Choose an option: ")
        return option

def import_students(file_path):
    students_list = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                students = line.strip().split(',')
                for student in students:
                    if student != "":
                        students_list[student] = True
            print("The student list was successfully imported.")
    except FileNotFoundError:
        print("File does not exist. Starting with an empty list.")
    return students_list

def add_student(students_list, file_lista_studentow):
    with open(file_lista_studentow, "a") as file:
        name = input("Enter the first and last name of the student to add: ")
        students_list[name] = True
        file.write(name + ",")
    print("The student was successfully added.")
    return students_list

def remove_student(file_path, students_list):
    name = input("Enter the first and last name of the student to remove: ")
    if name in students_list:
        students_list.pop(name)
    else:
        print("There is no such student in the database.")
    with open(file_path, "w") as file:
        for student in students_list.keys():
            file.write(student + ",")
    print("The student was removed.")

def export_students(file_path, students_list):
    with open(file_path, "w") as file:
        file.write(f"{datetime.now()}\n")
        for student, attendance in students_list.items():
            status = "present" if attendance else "absent"
            file.write(f"{student:<25} - {status}\n")
    print("The student list was successfully saved.")

def check_students(students_list):
    for student in students_list:
        print(f"Is {student} present? ")
        attendance = input("Y/N: ")
        if attendance.upper() == 'Y':
            students_list[student] = True
        elif attendance.upper() == 'N':
            students_list[student] = False
        else:
            print(f"Invalid choice for {student}. Marking as absent by default.")
            students_list[student] = False

def edit_students(students_list):
    name = input("Enter the student's name: ")
    attendance = input("Was the student present? Y/N: ")
    if attendance.upper() == 'Y':
        students_list.update({name : True})
    else:
        students_list.update({name : False})

def Main():

    file_list_of_students = 'students.txt'
    file_attendance = 'studentsAttendance.txt'
    students_list = {}

    while True:
        option = menu()
        if option == '1':
            students_list = import_students(file_list_of_students)
        elif option == '2':
            add_student(students_list, file_list_of_students)
        elif option == '3':
            check_students(students_list)
        elif option == '4':
            edit_students(students_list)
        elif option == '5':
            remove_student(file_list_of_students, students_list)
        elif option == '6':
            export_students(file_attendance, students_list)
        elif option == '7':
            exit()
        else:
            print("Invalid choice")

if __name__ == '__main__':
    Main()

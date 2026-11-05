from numpy import single


students = [
    {"id": 101, "name": "John", "department": "CT"},
    {"id": 102, "name": "akhil", "department": "EC"},
    {"id": 103, "name": "ananya", "department": "EL"}
]


def add_student():
    name = input("Enter the name: ")
    std_id = int(input("Enter the id: "))
    department = input("Enter the department: ")
    students.append({"id": std_id,"name": name,"department": department})


def display_students():
    print(f"{'id':^4}{'name':^10}{'department':^12}")
    print('-' * 26)
    for student in students:
        print(f"{student['id']:^4}{student['name']:^10}{student['department']:^12}")
    print('-' * 26)
    print(f"Total count: {len(students):>7}")


def edit_student():
    display_students()
    std_id = int(input("Enter the id to edit: "))
    for student in students:
        if student["id"] == std_id:
            student["name"] = input("Enter the new name: ")
            student["department"] = input("Enter the new department: ")
            print("Student updated successfully!")
            return
    print("Student not found!")


def delete_student():
    display_students()
    std_id = int(input("Enter the id to delete: "))
    for student in students:
        if student["id"] == std_id:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")


while True:
    choice = int(input(
        "\n1. Add a student\n"
        "2. Display students\n"
        "3. Edit a student\n"
        "4. Delete a student\n"
        "5. Exit\n"
        "Enter your choice: "
    ))

    match choice:
        case 1:
            add_student()
        case 2:
            display_students()
        case 3:
            edit_student()
        case 4:
            delete_student()
        case 5:
            break
        case _:
            print("Invalid choice")



            
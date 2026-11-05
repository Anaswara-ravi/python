students = []

while True:
    choice = input("1.add a student name:\n2.display student name\n3.update a student\n4.remove the student\n5.exit\nenter your choice: ")

    match choice:
        case "1":
            student_name = input("enter the name: ")
            students.append(student_name)
        case "2":
            print(f"{'sl.no':<10}{'name':<10}")
            for index, student in enumerate(students):
                print(f"{index + 1:<10}{student:<10}")
            print(f"total names: {len(students):<5}")
        case "3":
            print(f"{'sl.no':<10}{'name':<10}")
            for index, student in enumerate(students):
                print(f"{index + 1:<10}{student:<10}")
            edit_index = int(input("enter the sl.no. of the name you want to edit: ")) - 1
            edit_id = input("enter the u want to edit ")
            students[edit_index] = edit_i
        case "4":
            print(f"{'sl.no':<10}{'name':<10}")
            for index, student in enumerate(students):
                print(f"{index + 1:<10}{student:<10}")
            del_index = int(input("enter the sl.no. of the name you want to remove: ")) - 1
            students.pop(del_index)
        case "5":
            print("exiting....")
            break
        case _:
            print("invalid")


students = [
    {'id': 1, 'name': 'abhi', 'course': 'python'},
    {'id': 2, 'name': 'rahul', 'course': 'java'},
    {'id': 3, 'name': 'ARTHIK', 'course': 'python'}
]

while True:
    choice = input("1.add 2.display 3.update 4.delete 5.exit: ")

    match choice:

        case "1":
            id = input("enter student id: ")
            name = input("enter the name: ")
            rno = input("enter the rno: ")
            course = input("enter the course: ")

            students.append({
                "id": id,
                "name": name,
                "rno": rno,
                "course": course
            })

            print("Student added successfully")

        case "2":
            print(f"{'sl.no':<10}{'id':<10}{'name':<10}{'rno':<10}{'course':<10}")

            for index, student in enumerate(students):
                print(f"{index+1:<10}{student['id']:<10}{student['name']:<10}{student.get('rno', '-'):<10}{student['course']:<10}")

            print(f"Total students: {len(students)}")

        case "3":
            for index, student in enumerate(students):
                print(index+1, student['id'], student['name'], student.get('rno', '-'), student['course'])

            edit_id = input("Enter the id of the student: ")

            for student in students:
                if str(student['id']) == edit_id:
                    student['name'] = input("Enter new name: ")
                    student['rno'] = input("Enter new rno: ")
                    student['course'] = input("Enter new course: ")

                    print("Student updated successfully")
                    break
            else:
                print("Student not found")

        case "4":
            for index, student in enumerate(students):
                print(index+1, student['id'], student['name'], student.get('rno', '-'), student['course'])

            del_id = input("Enter the id of the student: ")

            for student in students:
                if str(student['id']) == del_id:
                    students.remove(student)
                    print("Student deleted successfully")
                    break
            else:
                print("Student not found")

        case "5":
            print("Exiting the program-----------")
            break

        case _:
            print("Invalid choice")

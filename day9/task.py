
books = [
    {'id': 101, 'name': 'Python Basics', 'author': 'John Smith', 'category': 'Programming', 'price': 450, 'copies': 5},
    {'id': 102, 'name': 'Web Development', 'author': 'David Miller', 'category': 'Technology', 'price': 550, 'copies': 3}
]

while True:
    choice = input("1.add 2.display 3.update 4.delete 5.exit: ")

    match choice:

        case "1":
            id = input("Enter book id: ")
            name = input("Enter book name: ")
            author = input("Enter author name: ")
            category = input("Enter category: ")
            price = int(input("Enter price: "))
            copies = int(input("Enter number of copies: "))

            books.append({
                "id": id,
                "name": name,
                "author": author,
                "category": category,
                "price": price,
                "copies": copies
            })

            print("Book added successfully")

        case "2":
            print(f"{'sl.no':<10}{'id':<10}{'name':<22}{'author':<20}{'category':<18}{'price':<10}{'copies':<10}")

            for index, book in enumerate(books):
                print(f"{index+1:<10}{book['id']:<10}{book['name']:<22}{book['author']:<20}{book['category']:<18}{book['price']:<10}{book['copies']:<10}")

            print(f"Total books: {len(books)}")

        case "3":
            for index, book in enumerate(books):
                print(index+1, book['id'], book['name'], book['author'], book['category'], book['price'], book['copies'])

            edit_id = input("Enter the id of the book: ")

            for book in books:
                if str(book['id']) == edit_id:
                    book['name'] = input("Enter new book name: ")
                    book['author'] = input("Enter new author name: ")
                    book['category'] = input("Enter new category: ")
                    book['price'] = int(input("Enter new price: "))
                    book['copies'] = int(input("Enter new copies: "))

                    print("Book updated successfully")
                    break
            else:
                print("Book not found")

        case "4":
            for index, book in enumerate(books):
                print(index+1, book['id'], book['name'], book['author'], book['category'], book['price'], book['copies'])

            del_id = input("Enter the id of the book: ")

            for book in books:
                if str(book['id']) == del_id:
                    books.remove(book)
                    print("Book deleted successfully")
                    break
            else:
                print("Book not found")

        case "5":
            print("Exiting the program-----------")
            break

        case _:
            print("Invalid choice")

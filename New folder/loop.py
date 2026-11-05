#1
for i in range(1, 11):
    print(i)

#2

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

  #3

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum is", total)



#4

n = int(input("Enter how many numbers: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c



#5

for i in range(1, 5):
    if i % 2 != 0:
        print("*")
    else:
        print("**")



#6


text = input("Enter a string: ")
reverse = ""

for i in text:
    reverse = i + reverse

print(reverse)



#7

for i in range(2, 51, 2):
    print(i)



#8

n = int(input("Enter a number: "))

while n >= 1:
    print(n)
    n = n - 1


#9


n = int(input("Enter a number: "))
fact = 1

while n > 0:
    fact = fact * n
    n = n - 1

print("Factorial is", fact)


#11

n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits:", count)


#12

while True:
    text = input("Enter something: ")

    if text == "exit":
        break

    print(text)



#13

num = [10, 20, 30, 40, 50]

for i in num:
    if i == 30:
        break
    print(i)



#14

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)


#15

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


#16


day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")


#17


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")


#18

marks = int(input("Enter marks: "))

match marks:
    case marks if marks >= 90:
        print("Grade A")
    case marks if marks >= 80:
        print("Grade B")
    case marks if marks >= 70:
        print("Grade C")
    case marks if marks >= 60:
        print("Grade D")
    case _:
        print("Fail")


#19


status = int(input("Enter status code: "))

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _ if 500 <= status <= 599:
        print("Server Error")
    case _ if status >= 400:
        print("Client Error")
    case _:
        print("Other Status")


#20

filename = input("Enter filename: ")
parts = filename.split(".")

match parts:
    case [name, "jpg"] | [name, "png"]:
        print("Image")
    case [name, "py"]:
        print("Python file")
    case _:
        print("Unknown file type")




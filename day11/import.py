from module import add,sub,mul,div
while True:
    choice=input('+ for addition\n-for substraction\n* for multiplication\n/ for division\nx for exit')
    n1=int(input("enter first number:"))
    n2=int(input("enter second number:"))

    match choice:
        case '+':
            print(add(n1,n2))
        case '-':
            print(sub(n1,n2))
        case '*':
            print(mul(n1,n2))
        case '/':
            print(div(n1,n2))
        case 'x':
            break
        case _:
            print("Invalid choice")
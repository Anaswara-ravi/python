# function is a reusable block of code to perform a specific task.

# def function_name(parameters):
#     function body
#     return 'result'

# function_name(argumentes)


# def greet():
#     print(f"hello ")
# greet()

# def greet(user):
#     print(f"hello, {user}")

# greet("john")


# result=greet("john")
# print(result)


# def greet(msg,user='guest'):
#     print(f"{msg},{user}")

# result1=greet('hello',"sree")
# result2=greet("welcome")

# print(result1)
# print(result2)


# n num of arguments varumbol use cheyunath-arbitery arguments 

# def add(a,*args):
#     total = 0
#     for n in args:
#         total += n
#     print(f"sum is:{total}")

# add(22,33,44)
# add(222,333,444,555,666)  #arbitary arguments
# add(1111,2222,333,4444,5555)



# def greet(msg,user):
#     return f"hello,{user}{msg}"
# print(greet(user="abhijith",msg="welcome")) #keyword argument



# def greet(**kwargs):
#     print(kwargs)
# print(user="karthik",msg="hello") #arbitary key word arguments














def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

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
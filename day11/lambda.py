# single line il function creation
#             ano function
#             function syntax ne ettavum small akki create cheyyan


# square=lambda x:x*x
# print(square(5))
# print(square(10))
# print(square(15))


# def type_of_num(num):
#     if num>0:
#         return "postitive"
#     elif num<0:
#         return "negative"
#     else:
#         return "zero"


# check_num=lambda num:"positive" if num>0 else "negative" if num<0 else "zero"
# print(check_num(5))
# print(check_num(-3))
# print(check_num(0))


# list ne single value lott convert reduce 

from functools import reduce
l1=[1,2,3,4,5]
square_numbers=list(map(lambda x:x*x,l1))
print(square_numbers)
even_number=filter(lambda x:x%2==0,l1)
print(list(even_number))
result=reduce(lambda x,y:x+y,l1)
print(result)
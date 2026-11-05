# List is a collection of heterogeneous data types

# Features of List in Python
# 1. Ordered
# 2. Indexed
# 3. Allows Duplication
# 4. Mutable


# num=[1,2,3,4,5,6,7]
# print(num)
# print(type(num))
# print(len(num))
# print(num[6])
# print(num[-1])
# print(num[-2])
# print(num[1:6])
# print(num[:-2])
# print(num[4:])
# print(num[::2])
# print(num[::-1])
# print(num[::-2])
# num[4]=100
# num.append(88)
# num.append(65)
# num.insert(2,99)
# num.extend([4,6,7])#multiple data anell use append allel extend


# print(num)

# even = 0

# # for n in num:
# #     if n % 2 == 0:
# #         even += 1

# # print(even)

# num.remove(6)
# print(num)
# num.pop()#last no pop akkum
# # num.clear()
# del num[4]
# print(num)


# l2=[]
# l3=list(num)
# print(l3)
# print(l3 is num)

# print(num.count(99))

# print(num.index(99))

# print(2 in num)

# print(2 not in num)

# l4=num.copy()
# l4[1]="abhi"
# print(l4 is num)
# num.sort(reverse=True)
# print(l4)

# ls=[[1,2,3],[4,5,6],[7,8,9]]
# print(ls[1][2])
# ls[2][1]=55
# print(ls)
# for x in ls:
#     for n in x:
#         print(n)



# num=[1,2,3,4,5,6,7]
# square_num=[]
# for n in num:
#     square_num.append(n*n)
# print(f"square num:{square_num}")
# square_num


# num=[1,2,3,4,5,6,7]
# square_comp=[n*n for n in num]
# print(square_comp)




# syntax:

#     [expression for item in iterable if clause]



# num=[1,2,3,4,5,6,7]
# for n in num:
#     if n % 2 == 0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")



num = [1, 2, 3, 4, 5, 6, 7]
print("\n".join([
    f"{n} is {'even' if n % 2 == 0 else 'odd'}"
    for n in num
]))




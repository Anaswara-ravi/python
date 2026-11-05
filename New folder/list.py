#1

numbers = [10, 5, 25, 8, 15]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest number is", largest)



#2

numbers = [10, 5, 25, 8, 15]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("Largest number is", smallest)



#3

numbers = [1, 2, 3, 4, 5]
total = 0

for i in numbers:
    total = total + i

print("Sum is", total)


#4

numbers = [10, 20, 30, 40, 50]
total = 0

for i in numbers:
    total = total + i

average = total / len(numbers)

print("Average is", average)


#5


numbers = [1, 2, 3, 4, 5]
rev = []

for i in numbers:
    rev.insert(0, i)

print(rev)


#6

numbers = [1, 2, 2, 3, 4, 4, 5]
result = []

for i in numbers:
    if i not in result:
        result.append(i)

print(result)

#7

numbers = [10, 20, 50, 40, 30]

numbers.sort()
print(numbers[-2])


#8

numbers = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)


#9

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print(common)


#10


list1 = [1, 2, 3]
list2 = [3, 4, 5]

result = list1.copy()

for i in list2:
    if i not in result:
        result.append(i)

print(result)


#11


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for i in matrix:
    for n in i:
        total = total + n

print("Sum is", total)

#12

matrix = [
    [1, 2, 3],
    [10, 5, 6],
    [7, 8, 9]
]

largest = matrix[0][0]

for i in matrix:
    for n in i:
        if n > largest:
            largest = n

print("Largest is", largest)









#1

numbers = [10, 5, 25, 8, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element is", largest)


#2

numbers = [10, 5, 25, 8, 15]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element is", smallest)



#3


numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
    total = total + num

print("Sum is", total)



#4

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average is", average)



#5

numbers = [1, 2, 3, 4, 5]

reversed_list = []

for num in numbers:
    reversed_list.insert(0, num)

print(reversed_list)


#6

numbers = [1, 2, 2, 3, 4, 4, 5]
new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print(new_list)


#7

numbers = [10, 20, 50, 40, 30]
numbers.sort()

print(numbers[-2])



#8

numbers = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)



#8



list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)


#9


list1 = [1, 2, 3]
list2 = [3, 4, 5]
new_list = []

for num in list1:
    if num not in new_list:
        new_list.append(num)

for num in list2:
    if num not in new_list:
        new_list.append(num)

print(new_list)



# set is an unorder collection of unique elements 
# -Unordered
# -unindexed
# -mutable
# -it does not allow duplicate ValueError






# student={"hari","manu","abhi","akhil"}
# print(student)
# print(type(student))
# n={}  #this 
# print(type(n))
# student.add("rahul")
# student.remove("abhi")#remove the existing value only in the set otherwisw show error
# student.remove("rahul")
# student.discard("manu")#no show the error
# student.discard("abhy")
# student.pop()#randomly delete
# student.clear()



# # update
# student.remove("hari")
# student.add("sreerag")
# print(student)
# print(len(student))



# for students in student:
#     print(students) 






# actor_1={"vijay","surya","mohanlal","kunjako"}
# actor_2={"dhanush","vijay","abhishek","surya"}


# print(actor_1.union(actor_2)) #add this two set
# print(actor_1 | actor_2)

# print(actor_1.intersection(actor_2)) #repeat value display
# print(actor_1 & actor_2)

# print(actor_1.difference(actor_2))
# print(actor_1 - actor_2)

# print(actor_1.symmetric_difference(actor_2))#over all not repeat values
# print(actor_1 ^ actor_2)



# actor_1.update(actor_2)
# actor_1.intersection_update(actor_2)#insertsection and add to actor2
# actor_1.symmetric_difference_update(actor_2)




# num={1,2,3,4,5,6,9,10}
# even_num={2,4,5,1}


my_set = {1, 2, 3}
my_list = [4, 5, 6]

my_set.add(my_list)

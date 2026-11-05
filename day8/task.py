python_students = {"Arun", "Megha", "Rahul", "Sneha"}
analytics_students = {"Sneha", "Rahul", "Aman", "Diya"}
#1 
print(python_students.intersection(analytics_students))
#2
for num in python_students:
    print(num)

#3

for num in analytics_students:
    print(num)

#4

print(python_students.symmetric_difference(analytics_students))

#5
print(python_students.union(analytics_students))






#1

customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
customer2 = {"Apple", "Vivo", "Oppo", "Samsung"} 

#1
print(customer1.intersection(customer2))

#2

print(customer1.union(customer2))

#3

print(customer1.difference(customer2))

#4



print(customer1.symmetric_difference(customer2))




design_team = {"Figma", "Photoshop", "Canva", "Illustrator"}
marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"}

# 1.
print(design_team.intersection(marketing_team))

# 2
print(design_team.difference(marketing_team))

# 3
print(design_team.union(marketing_team))

# 4
print(design_team.symmetric_difference(marketing_team))





electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"}
accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"}

# 1. 
print(electronics.intersection(accessories))

# 2. 
print(electronics.difference(accessories))

# 3. 
print(electronics.union(accessories))

# 4. 
print(electronics.symmetric_difference(accessories))



employee1 = {"Python", "Java", "SQL", "C"}
employee2 = {"Python", "JavaScript", "SQL", "Go"}

# 1. 
print(employee1.intersection(employee2))

# 2. 
print(employee1.difference(employee2))

# 3. F
print(employee1.union(employee2))

# 4.
print(employee1.symmetric_difference(employee2))


friend1 = {"Netflix", "Prime", "Hotstar", "SonyLiv"}
friend2 = {"Netflix", "Zee5", "Prime", "JioCinema"}

# 1. 
print(friend1.intersection(friend2))

# 2. 
print(friend1.difference(friend2))

# 3. 
print(friend1.union(friend2))

# 4. 
print(friend1.symmetric_difference(friend2))


available_products = {"Laptop", "Mouse", "Keyboard", "Monitor"}
sold_products = {"Mouse", "Monitor"}

# 1. 
print(available_products.difference(sold_products))

# 2. 
print(sold_products)

# 3. 
available_products.add("Printer")
print(available_products)

# 4. 
available_products.remove("Keyboard")
print(available_products)


music_event = {"Anu", "David", "Riya", "Sam"}
dance_event = {"Riya", "Sam", "Karthik", "John"}

# 1. 
print(music_event.intersection(dance_event))

# 2. 
print(music_event.difference(dance_event))

# 3. 
print(dance_event.difference(music_event))

# 4. 
print(music_event.union(dance_event))


campaign_A = {"user101", "user102", "user103", "user104"}
campaign_B = {"user103", "user104", "user105", "user106"}

# 1. 
print(campaign_A.intersection(campaign_B))

# 2. 
print(campaign_A.difference(campaign_B))

# 3. 
print(campaign_A.union(campaign_B))

# 4. 
print(campaign_A.symmetric_difference(campaign_B))



restaurant1 = {"Burger", "Pizza", "Fries", "Pasta"}
restaurant2 = {"Pizza", "Sandwich", "Pasta", "Momos"}

# 1. 
print(restaurant1.intersection(restaurant2))

# 2. 
print(restaurant1.difference(restaurant2))

# 3.
print(restaurant2.difference(restaurant1))

# 4. 
print(restaurant1.union(restaurant2))

# 5. 
print(restaurant1.symmetric_difference(restaurant2))
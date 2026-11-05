#1


# mark=int(input("enter ur mark:"))
# if mark>=90 and mark<=100:
#     print("A+")
# elif mark>=80 and mark<=89:
#     print("A")
# elif mark>=70 and mark<=79:
#     print("B")
# elif mark>=60 and mark<=69:
#     print("c")
# elif mark>=50 and mark<=59:
#     print("D")
# else:
#     print("failed try again")


# #2
# balance=int(input("enter the balanced amount:"))
# withdraw=int(input("enter the price:"))
# if withdraw>balance:
#     print("Insufficient Balance ")
# elif withdraw % 100 != 0:
#     print("enter an amount in multiples of 100")
# else:
#     print("Withdrawal Successful ")

#3

# bill = int(input("Enter your total bill amount: "))

# if bill >= 5000:
#     charge = 0
#     print("Free delivery")

# elif bill >= 2000:
#     charge = 50
#     print("50 delivery charge")

# else:
#     charge = 100
#     print("100 delivery charge")

# total = bill + charge

# print("Delivery charge:", charge)
# print("Total bill:", total)

#4
# score=int(input("enter ur score:"))
# if score>=90:
#     print(" Excellent ")
# elif score>=75:
#     print("Very Good ")
# elif score>=60:
#     print(" Good ")
# elif score>=40:
#     print("Needs Improvement ")
# else: 
#     print("Poor ")

#5

# units = int(input("Enter the units consumed: "))

# if units <= 100:
#     bill = units * 2

# elif units <= 200:
#     bill = (100 * 2) + ((units - 100) * 3)

# elif units <= 400:
#     bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

# else:
#     bill = (100 * 2) + (100 * 3) + (200 * 5) + ((units - 400) * 7)

# print("Electricity bill: ₹", bill)


#6

# ticket=int(input("enter ur age:"))
# if ticket<5:
#     fee=0
#     print(" free")
# elif ticket<=12:
#     fee=100
# elif ticket>=59:
#     fee=200
# else: 
#     fee=120
# print("total price:",fee)


#7


# speed = int(input("Enter vehicle speed: "))

# if speed <= 60:
#     print("No fine")

# elif speed <= 80:
#     print("Fine: ₹500")

# elif speed <= 100:
#     print("Fine: ₹1000")

# else:
#     print("Fine: ₹2000")
#     print("License Review")

#8

# bill = int(input("Enter the total bill amount: "))

# if bill >= 5000:
#     discount = bill * 20 / 100

# elif bill >= 3000:
#     discount = bill * 15 / 100

# elif bill >= 1000:
#     discount = bill * 10 / 100

# else:
#     discount = 0

# final_bill = bill - discount

# print("Discount amount:", discount)
# print("Final bill amount:", final_bill)

#9


# score = int(input("Enter your entrance exam score: "))

# if score >= 90:
#     print("Direct Admission")

# elif score >= 75:
#     print("Admission + Interview")

# elif score >= 60:
#     print("Waitlisted")

# else:
#     print("Not Eligible")


#10


# score = int(input("Enter your credit score: "))
# default = input("Do you have an existing loan default? (yes/no): ")

# if default == "yes":
#     print("Loan Approval Requires Manual Review")

# elif score >= 750:
#     print("Low Risk")

# elif score >= 650:
#     print("Medium Risk")

# elif score >= 550:
#     print("High Risk")

# else:
#     print("Very High Risk")


#11


# room = input("Enter room type (Standard/Deluxe/Suite): ")
# nights = int(input("Enter number of nights: "))

# if room == "Standard":
#     price = 2000
# elif room == "Deluxe":
#     price = 3500
# elif room == "Suite":
#     price = 5000
# else:
#     price = 0
#     print("Invalid room type")

# if price > 0:
#     total = price * nights

#     if nights > 5:
#         discount = total * 10 / 100
#     else:
#         discount = 0

#     final_bill = total - discount

#     print("Total room cost:", total)
#     print("Discount:", discount)
#     print("Final bill:", final_bill)


#12,


# salary = int(input("Enter annual salary: "))
# score = int(input("Enter performance score: "))

# if score >= 90:
#     bonus = salary * 20 / 100

# elif score >= 75:
#     bonus = salary * 15 / 100

# elif score >= 60:
#     bonus = salary * 10 / 100

# else:
#     bonus = 0

# print("Annual Bonus:", bonus)

#13


# data = float(input("Enter monthly data usage in GB: "))

# if data < 5:
#     print("Basic Plan - ₹199")

# elif data <= 20:
#     print("Standard Plan - ₹399")

# elif data <= 50:
#     print("Premium Plan - ₹699")

# else:
#     print("Unlimited Plan - ₹999")


#14


# hours = int(input("Enter parking duration in hours: "))
# vehicle = input("Is it an electric vehicle? (yes/no): ")

# # if hours <= 2:
#     fee = 30
# elif hours <= 5:
#     fee = 50
# elif hours <= 10:
#     fee = 100
# else:
#     fee = 150

# if vehicle == "yes":
#     discount = fee * 20 / 100
# else:
#     discount = 0

# final_fee = fee - discount

# print("Parking fee:", fee)
# print("Discount:", discount)
# print("Final parking fee:", final_fee)


#!5


# theory = int(input("Enter theory mark: "))
# practical = int(input("Enter practical mark: "))

# if theory < 40 or practical < 40:
#     print("Fail")

# else:
#     average = (theory + practical) / 2
#     print("Average:", average)

#     if average >= 75:
#         print("Distinction")

#     elif average >= 60:
#         print("First Class")

#     elif average >= 50:
#         print("Second Class")

#     else:
#         print("Pass")

#16

# weight = float(input("Enter baggage weight in kg: "))
# travel_class = input("Enter travel class (Economy/Business): ").lower()

# if travel_class == "business":
#     free_limit = 25
# else:
#     free_limit = 15

# if weight <= free_limit:
#     charge = 0
# elif weight <= 20:
#     charge = 500
# elif weight <= 30:
#     charge = 1000
# else:
#     charge = 2000

# print("Baggage charge: ₹", charge)

#17

# days = int(input("Enter days since purchase: "))
# unused = input("Is the product unused? (yes/no): ").lower()
# returnable = input("Is the product returnable? (yes/no): ").lower()

# if days > 7:
#     print("Return Rejected: Purchase was made more than 7 days ago.")
# elif unused != "yes":
#     print("Return Rejected: Product is used.")
# elif returnable != "yes":
#     print("Return Rejected: Product is not returnable.")
# else:
#     print("Return Approved")

#18

# salary = float(input("Enter annual salary: "))

# if salary <= 300000:
#     tax = 0
# elif salary <= 600000:
#     tax = salary * 5 / 100
# elif salary <= 1000000:
#     tax = salary * 10 / 100
# else:
#     tax = salary * 20 / 100

# final_salary = salary - tax

# print("Tax amount: ₹", tax)
# print("Salary after tax: ₹", final_salary)


#19
# distance = float(input("Enter distance in km: "))
# peak = input("Is it peak hour? (yes/no): ").lower()

# if distance <= 5:
#     fare = 100
# elif distance <= 15:
#     fare = 100 + (distance - 5) * 15
# elif distance <= 30:
#     fare = 100 + (10 * 15) + (distance - 15) * 12
# else:
#     fare = 100 + (10 * 15) + (15 * 12) + (distance - 30) * 10

# if peak == "yes":
#     fare = fare + (fare * 20 / 100)

# print("Final ride fare: ₹", fare)

#20

# available_leave = int(input("Enter available leave days: "))
# requested_leave = int(input("Enter requested leave days: "))

# if requested_leave > available_leave:
#     print("Leave Rejected")
# elif requested_leave <= 3:
#     print("Leave Automatically Approved")
# elif requested_leave <= 7:
#     print("Manager Approval Required")
# else:
#     print("HR Approval Required")



















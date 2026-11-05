#1. Write a program to add two numbers entered by the user.
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# print(a+b)

#2. Write a program to find the difference between two numbers. 

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# print("difference:",a-b)

# 3. Write a program to multiply three numbers

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# print("result:",a*b*c)

# 4. Write a program to divide one number by another. 

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# print("Division:",a/b)


# 5. Write a program to calculate the square of a number.
# num=int(input("enter the  number:"))
# print("square:",num*num)


# 6. Write a program to calculate the cube of a number. 

# num=int(input("enter the  number:"))
# print("cube:",num*num*num)

# 7. Write a program to calculate the average of three numbers. 

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# print("result:",(a+b+c)/3)


# # 8. Calculate the total price of 5 notebooks.

# price = int(input("Enter the price of one notebook: "))
# total = price * 5
# print("Total price:", total)



# 9. Find the quotient and remainder.

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print("Quotient:", a // b)
# print("Remainder:", a % b)



# 10. Calculate completely filled boxes and leftover chocolates.

# chocolates = 47
# box = 6
# print("Completely filled boxes:", chocolates // box)
# print("Chocolates left over:", chocolates % box)


# 11. Convert minutes into complete hours and remaining minutes

# minutes = int(input("Enter the minutes: "))
# hours = minutes // 60
# remaining_minutes = minutes % 60
# print("Hours:", hours)
# print("Remaining minutes:", remaining_minutes)


# 12. Convert 367 seconds into minutes and remaining seconds

# seconds = 367
# minutes = seconds // 60
# remaining_seconds = seconds % 60
# print("Minutes:", minutes)
# print("Remaining seconds:", remaining_seconds)

# 13. A teacher wants to distribute 53 students into groups of 8. Calculate the number of complete groups and the students left over. 

# students = 53
# group = 8
# print("Complete groups:", students // group)
# print("Students left over:", students % group)


# 14. Write a program to extract the last digit of a positive integer using the modulus operator. 

# num=123
# last_num=num%10
# print("last number is:",last_num)


# 15. Write a program to remove the last digit of a positive integer using floor division. 

# num=123
# last_num=num//10
# print("last number is:",last_num)

# 16. Shopping bill: A customer buys 3 pens costing ₹15 each and 2 notebooks costing ₹40 each. Calculate the total bill.

# pen=15
# notebook=40
# total=(pen*3)+(notebook*2)
# print("total price",total)

# 17. Salary calculation: An employee earns ₹800 per day. Calculate their salary for 26 working days. 

# per_day=800
# total=800*26
# print("monthly salray:",total)


# 18. Distance conversion: Convert a distance given in kilometers into meters and centimeters. 

# km = 5
# meters = km * 1000
# centimeters = km * 100000
# print("Distance in meters:", meters)
# print("Distance in centimeters:", centimeters)


# 19. Rectangle: Accept the length and width of a rectangle and calculate its area and perimeter. 

# length=int(input("enter the length:"))
# width=int(input("enter the width:"))
# area=length*width
# perimeter=2*(length+width)
# print("area",area)
# print("perimeter:",perimeter)


# 20. Simple interest: Accept the principal amount, annual interest rate, and time in years. Calculate the simple interest using: SI=(P×R×T) /100 

# p = float(input("Enter principal amount: "))
# r = float(input("Enter annual interest rate: "))
# t = float(input("Enter time in years: "))
# si = (p * r * t) / 100
# print("Simple Interest:", si)


# 21. Bill sharing: Accept a restaurant bill and the number of friends. Calculate how much each friend should pay if the bill is shared equally. 

# bill=int(input("bill amount:"))
# num_frd=int(input("enter number of freds:"))
# pay=bill/num_frd
# print("each one: ",pay)

# 22. Travel calculation: A car travels 180 km using 12 liters of fuel. Calculate its mileage in km per liter. 

# distance = 180
# fuel = 12
# mileage = distance / fuel
# print("Car mileage:", mileage, "km/l")


# 23. Unit price: Accept the total price of a packet of rice and its weight in kilograms. Calculate the price per kilogram.

# total_price = float(input("Enter total price of rice: "))
# weight = float(input("Enter weight in kg: "))
# price = total_price / weight
# print("Price per kg:", price)


# 24. Time conversion: Accept a total number of hours and convert it into complete days and remaining hours. 


# hours = int(input("Enter total hours: "))
# days = hours // 24
# remaining_hours = hours % 24
# print("Complete days:", days)
# print("Remaining hours:", remaining_hours)


# 25. Power calculation: Accept a number and an exponent, then calculate the result using the ** operator. 

# num = int(input("Enter a number: "))
# exponent = int(input("Enter an exponent: "))
# result = num ** exponent
# print("Result:", result)











# //1. College Event Registration A college is organizing a technical workshop. A student can register if: ● Their age is between 18 and 25, and ● They are currently a student. Accept the student's age and student status and display whether they are eligible for registration. 

# age = int(input("Enter your age: "))
# status = input("Enter the status (true/false): ")
# eligible = (age >= 18 and age <= 25) and status == "true"
# print(eligible)

# 2. Online Shopping Discount An e-commerce website provides a discount when: ● The order value is ₹3,000 or more, or ● The customer is a premium member. Accept the order amount and membership status. Display whether the customer qualifies for the discount. 


# amount = int(input("Enter order amount: "))
# status = input("Are you a premium member (true/false): ")
# discount = (amount >= 3000) or (status == "true")
# print("Eligible for discount:", discount)



# 3. Airport Check-in A passenger can proceed with online check-in if: ● Their ticket is confirmed, ● Their passport is valid, and ● Their departure is more than 2 hours away. Accept the three required values and determine whether online check-in is available. 


# ticket = input("Is ticket confirmed (true/false): ")
# passport = input("Is passport valid (true/false): ")
# hours = float(input("Hours left for departure: "))
# checkin = (ticket == "true") and (passport == "true") and (hours > 2)
# print("Online check-in available:", checkin)


# 4. Movie Ticket Booking A cinema offers a special ticket price to customers who are: ● Below 12 years old, or ● 60 years old or above. Accept the customer's age and determine whether they qualify for the special ticket price. age = int(input("Enter your age: "))

# age = int(input("Enter your age: "))
# special_price = (age < 12) or (age >= 60)
# print("Eligible for special ticket price:", special_price)


# 5. Bank Loan Pre-Eligibility A bank wants to perform an initial loan eligibility check. A customer qualifies if: ● Monthly income is at least ₹40,000, ● Credit score is at least 700, and ● The customer does not have an existing loan default. Accept these details and display the eligibility result. 

# income = int(input("Enter monthly income: "))
# score = int(input("Enter credit score: "))
# default = input("Do you have an existing loan default (true/false): ")
# eligible = (income >= 40000) and (score >= 700) and (default == "false")
# print("Loan eligible:", eligible)



# 6. Food Delivery Free Shipping A food delivery application provides free delivery when: ● The order amount is ₹500 or more, or ● The customer has a premium membership. However, free delivery is not available when the restaurant has temporarily disabled delivery. Accept the required information and determine whether free delivery is available.

# amount = int(input("Enter order amount: "))
# premium = input("Are you a premium member (true/false): ")
# delivery = input("Is delivery available (true/false): ")
# free_delivery = (amount >= 500 or premium == "true") and delivery == "true"
# print("Free delivery available:", free_delivery)


# 7. Employee Work-from-Home Eligibility An employee can work from home if: ● They have completed at least 6 months in the company, and ● Their current project allows remote work. Accept the employee's experience and project policy and determine whether they can work from home.


# months = int(input("Enter experience in months: "))
# remote = input("Does the project allow remote work (true/false): ")
# eligible = (months >= 6) and (remote == "true")
# print("Work from home eligible:", eligible)


# 8. Hotel Room Booking A hotel allows a customer to book a room if: ● The room is available, and ● The customer has a valid payment method. However, bookings are not allowed if the hotel has temporarily stopped accepting reservations. Determine whether the booking can proceed. 


# room = input("Is the room available (true/false): ")
# payment = input("Is the payment method valid (true/false): ")
# booking = input("Is the hotel accepting reservations (true/false): ")
# eligible = (room == "true") and (payment == "true") and (booking == "true")
# print("Booking can proceed:", eligible)


# 9. Online Exam Access A student can start an online examination if: ● They are logged into their account, ● Their exam registration is confirmed, ● The examination is currently active, and ● Their account is not blocked. Accept these details and determine whether the student can access the exam.

# login = input("Are you logged in (true/false): ")
# registration = input("Is exam registration confirmed (true/false): ")
# exam = input("Is the exam active (true/false): ")
# blocked = input("Is your account blocked (true/false): ")
# access = (login == "true") and (registration == "true") and (exam == "true") and (blocked == "false")
# print("Can access exam:", access) 


# 10. Gym Membership Plan A gym provides a premium membership upgrade if: ● The member has been subscribed for at least 1 year, and ● Their current membership is active. Alternatively, a member can receive the upgrade if they have purchased a yearly plan. Determine whether the member qualifies for the premium upgrade. 


# years = int(input("Enter subscription period in years: "))
# active = input("Is membership active (true/false): ")
# yearly = input("Have you purchased a yearly plan (true/false): ")
# upgrade = ((years >= 1) and (active == "true")) or (yearly == "true")
# print("Eligible for premium upgrade:", upgrade)



# 11. Ride Booking Application A customer can book an immediate ride if: ● Their pickup location is within the service area, and ● A driver is currently available. Alternatively, the customer can make a scheduled booking if scheduled rides are enabled. Determine whether the customer can make a booking. 

# location = input("Is pickup location within service area (true/false): ")
# driver = input("Is a driver available (true/false): ")
# scheduled = input("Are scheduled rides enabled (true/false): ")
# booking = ((location == "true") and (driver == "true")) or (scheduled == "true")
# print("Booking available:", booking)


# 12. E-commerce Product Return An online store accepts a product return if: ● The product was purchased within the last 7 days, ● The product is unused, and ● The product is eligible for return. Determine whether the customer's return request can be accepted. 


# days = int(input("Enter days since purchase: "))
# unused = input("Is the product unused (true/false): ")
# eligible = input("Is the product eligible for return (true/false): ")
# accepted = (days <= 7) and (unused == "true") and (eligible == "true")
# print("Return request accepted:", accepted)


# 13. Library Book Borrowing A student can borrow a book from the college library if: ● They have no overdue books, ● Their library membership is active, and ● The requested book is available. Accept the required information and determine whether the student can borrow the book.

# overdue = input("Do you have overdue books (true/false): ")
# membership = input("Is library membership active (true/false): ")
# book = input("Is the requested book available (true/false): ")
# borrow = (overdue == "false") and (membership == "true") and (book == "true")
# print("Can borrow book:", borrow)

# 14. Job Application Screening A company is looking for a Python developer. A candidate passes the initial screening if: ● They have at least 1 year of Python experience, and ● They know either Django or FastAPI. Additionally, candidates with 3 or more years of experience are automatically considered for the next stage. Determine whether the candidate qualifies for the next stage. 


# years = int(input("Enter Python experience in years: "))
# django = input("Do you know Django (true/false): ")
# fastapi = input("Do you know FastAPI (true/false): ")
# eligible = (years >= 1 and (django == "true" or fastapi == "true")) or (years >= 3)
# print("Qualified for next stage:", eligible)



# 15. Mobile Data Usage Alert A mobile application should display a warning when: ● The user's data usage has reached at least 90% of their monthly limit, or ● Their remaining data is less than 1 GB. However, the warning should not be displayed if the user has an unlimited data plan. Determine whether the warning should be triggered

# usage = float(input("Enter data usage percentage: "))
# remaining = float(input("Enter remaining data in GB: "))
# unlimited = input("Do you have unlimited data (true/false): ")
# warning = ((usage >= 90) or (remaining < 1)) and (unlimited == "false")
# print("Warning triggered:", warning)


# 16. Parking Lot Entry A vehicle can enter a parking facility if: ● The vehicle has a valid parking pass, or ● The driver is paying for visitor parking. However, entry is not permitted if the parking lot is full. Determine whether the vehicle can enter. 

# pass_valid = input("Do you have a valid parking pass (true/false): ")
# visitor = input("Are you paying for visitor parking (true/false): ")
# full = input("Is the parking lot full (true/false): ")
# entry = (pass_valid == "true" or visitor == "true") and (full == "false")
# print("Vehicle can enter:", entry)


# 17. Scholarship Eligibility A student is eligible for a scholarship if: ● Their academic score is at least 85%, and ● Their attendance is at least 75%. Students with an academic score of 95% or higher can qualify regardless of attendance. Determine whether the student is eligible. 


# score = int(input("Enter academic score: "))
# attendance = int(input("Enter attendance percentage: "))
# eligible = (score >= 85 and attendance >= 75) or score >= 95
# print("Scholarship eligible:", eligible)


# 18. Food Ordering – Restaurant Availability A customer can place an order if: ● The restaurant is currently open, ● The restaurant delivers to the customer's location, and ● The restaurant is accepting online orders. Determine whether the customer can place an order. 



# open_status = input("Is the restaurant open (true/false): ")
# delivery = input("Does the restaurant deliver to your location (true/false): ")
# online = input("Is the restaurant accepting online orders (true/false): ")
# can_order = (open_status == "true") and (delivery == "true") and (online == "true")
# print("Can place order:", can_order)



# 19. Smart Home Security A smart home system should activate an alert when: ● Motion is detected, and ● The security system is armed. It should also activate an alert when the main door is opened while the security system is armed. Determine whether the security alert should be triggered. 



# motion = input("Is motion detected (true/false): ")
# armed = input("Is the security system armed (true/false): ")
# door = input("Is the main door opened (true/false): ")
# alert = (motion == "true" and armed == "true") or (door == "true" and armed == "true")
# print("Security alert triggered:", alert)



# 20. Travel Insurance Eligibility A person can purchase a particular travel insurance plan if: ● Their age is between 18 and 65, ● Their trip duration is 30 days or less, and ● They are travelling to a country covered by the insurance. However, the plan is unavailable if the destination is currently excluded from coverage. Determine whether the person is eligible for the insurance plan. 


# age = int(input("Enter your age: "))
# days = int(input("Enter trip duration in days: "))
# covered = input("Is the country covered by insurance (true/false): ")
# excluded = input("Is the destination excluded from coverage (true/false): ")
# eligible = (age >= 18 and age <= 65) and (days <= 30) and (covered == "true") and (excluded == "false")
# print("Eligible for travel insurance:", eligible)

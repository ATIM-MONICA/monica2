#Qn1. The Volume of a sphere with radius r is (4/3)* pie * r**2.
#What is the volume of a sphere with radius 5?
#Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places.
radius = int(input("Enter radius of the sphere: "))
volume = (4/5)*22/7*radius**2
print(f"The volume of a sphere with radius {radius} is {volume:.2f} cubic meters")
#Qn2.Create a program to calculate the area of a triangle  (1/2 * base * height)
#Base and height should be entered using the keyboard.
base = int(input("Enter the base of a triangle: "))
height = int(input("Enter the height of a triangle: "))
area_of_a_triangle = (1/2*base*height)
print(f"The area of a triangle {area_of_a_triangle}")
#Qn3. WITI has tasked you to automate a simple grading system.
# As a python student, write a program using to display the grades that
# The students will be receiving based on the marks scored in a subject.
# The grades are:
# 90% - 100% Grade is A
# 80% - 89% Grade is B
# 70% - 79% Grade is C
# 60% - 69% Grade is D
# 50% - 59% Grade is E
# <50% Fail
marks_scored = float(input("Enter marks scored (0-100): "))
if 0 <= marks_scored <= 100:
    if marks_scored >= 90:
        grade =  'A'
    elif marks_scored >= 80:
        grade = 'B'
    elif marks_scored >= 70:
        grade = 'c'
    elif marks_scored >= 60:
        grade = 'D'
    elif marks_scored >= 50:
        grade = 'E'
    else:
        grade = 'Fail'
        print("Grade:", grade)
else:
    print("Invalid marks. Please enter the value between o and 100.")

#Qn4. WITI Academy is proposing a SACCO to help students save their money.
# Design a platform that will do the following.
# Welcome to, WITI Academy SACCO.
# 1. Deposit money
# 2. Withdraw money
# 3. Check balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
# If the students select 2, money sholub be withdrawn and a minimum withdrawal is 500.
# If the student select 3, the account balance should be displayed.
balance = 0
print("Welcome to WITI Academy SACCO")
print("\nPlease choose an option")
print("1. Deposit Money ")
print("2. Withdraw Money ")
print("3. Check Balance ")

choice = input("Enter your choice (1/2/3): ")
if choice == '1':
    amount = float(input("Enter amount to deposit: "))
    if amount >= 1000:
        balance += amount
        print(f"Successfully deposited {amount}. New balance is: {balance}.")
    else: 
        print("Minimum balance to deposit is 1000")
elif choice == '2':
    amount = float(input("Enter amount to withdraw: "))
    if amount == 500:
        if balance is amount:
            balance -= amount
            print(f"Successfully withdrew {amount}. New balance is {balance}.")
        else:
            print("Insufficient balance.")
else:
  print("Minimum withdrawal amount is 500.")
if choice == '3': # check balance
 print("Your current balance is {balance}.")
else:
 print("Invalid choice.")
 




        
    

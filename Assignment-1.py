print("hello world")

print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are")


import sys

print("Python Version:")
print(sys.version)

import datetime

now = datetime.datetime.now()
print("Current date and time:")
print(now)

import math

radius = float(input("Enter radius: "))
area = math.pi * radius ** 2

print("Area of circle is:", area)

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(last_name + " " + first_name)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 + num2

print("Addition is:", result)

marks = []
total = 0

for i in range(1, 6):
    mark = float(input(f"Enter marks of subject {i}: "))
    marks.append(mark)
    total += mark

percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")




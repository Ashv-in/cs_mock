import random

#Onboarding/Profile Creation

print("Welcome to ......!")
print("Let's get started")
print()

name = input("Enter your name: ")
print(f"Hey {name}, let's fill up some additional details to get upto speed with your past medical history")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

while True:
    history = input("Have u ever had any past serious illnesses? (Y/N) ").upper()
    if history=='Y':
        past_med = input("Enter your past conditions (separated with commas) ").split(', ')
        break
    elif history=='N':
        past_med = []
        print("That's great")
        break
    else:
        print("Please enter a valid input")

print("Almost done, please verify your email/phone number")
email = input("Enter a valid email ID: ")







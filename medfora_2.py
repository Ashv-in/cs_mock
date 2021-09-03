import random
from datetime import datetime

#Onboarding/Profile Creation

print("Welcome to Medfora!")
print("Let's get started")
print()

while True:
    option = input("Do you have an existing Medfora account? (Y/N) ").upper()
    if option=='N':
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

        print("Almost done, please verify your email and phone number")
        email = input("Enter a valid email ID: ")
        phone = int(input("Enter your mobile number: "))
        print("That's it, you're all set to go!")
        print("-------------------------------------------------------------")
        print()
        id = str(random.randint(10000,20000))+random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")+random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        break
    elif option=='Y':
        id = input("Please enter your ID: ").upper()
        break
    else:
        print("Please enter a valid input")


#functions for new prescriptions and lab reports

prescriptions_summary = []
reports_summary = []
prescriptions_detailed = []
reports_detailed = []

def newPrescription(hospital, doctor):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    patient_id = input("Enter patient ID: ").upper()
    pres = input("Enter prescription: ")
    prescriptions_summary.append(f"{dt_string}: {hospital} - {doctor}")
    prescriptions_detailed.append(f"{dt_string}: {hospital} - {doctor}\n{pres}")

def newReport(hospital, doctor):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    patient_id = input("Enter patient ID: ").upper()
    report = input("Enter lab report: ")
    reports_summary.append(f"{dt_string}: {hospital} - {doctor}")
    reports_detailed.append(f"{dt_string}: {hospital} - {doctor}\n{pres}")

def getPrescription(index):
    print(prescriptions_detailed[index-1])

def getReport(index):
    print(reports_detailed[index-1])


#user control

while True:
    print("1. Prescriptions\n2. Lab Reports\n3. Share profile")
    tab = int(input("Please choose an option to get started (1/2/3):")
    print()
    if tab==1:
        if len(prescriptions_summary)==0:
            print("No prescriptions")
        else:
            for i in range(1, len(prescriptions_summary)+1):
                print(i, prescriptions_summary[i-1])

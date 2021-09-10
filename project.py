# *********************************************************
# Program: YOUR_FILENAME.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TT0?
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211103139 | HANNAH SOFEA BINTI ROSLEE | 1211103139@student.mmu.edu.my | +60123616790
# Member_2: 1211103128 | MUHAMMAD AJWAD BIN MOHAMAD A'SIM | 1211103128@student.mmu.edu.my | +601154261979
# Member_3: 1211103138 | NURUL NABILAH BINTI MOHD NOOR HAKIM | 1211103138@student.mmu.edu.my | +60132027946
# Member_4: ID | NAME | EMAIL | PHONES
# *********************************************************
# Task Distribution
# Member_1:Account sign up & login authentication
# Member_2:Administrator assign appointment,create vaccination center & generate list
# Member_3:Public user update information & view appointment
# Member_4:
# *********************************************************

import sqlite3
from sqlite3.dbapi2 import SQLITE_SELECT, connect
connection = sqlite3.connect('user.db')
myCursor = connection.cursor()
#in user.db, it has one table(userdata) that contains(user_name text, user_age int, ic_number text, phone_number text, post_code int, home_address text, q1 text, q2 text, q3 text, q4 text, q5 text, q6 text, priority int)""") 

########## Hannah's part ##########
########################################################### FUNCTIONS FOR WELCOMEPAGE #########################################################################

def login_func(): #login page
    Phone = input('Enter your phone number: \n').strip()
    IC = input('Enter your IC number: \n').strip()
    
    retrieved_user_data = myCursor.execute("SELECT * FROM userdata WHERE ic_number= :IC", {'IC':IC}) #to search the ic number inputted == with in the database or not

    for value in retrieved_user_data:
        icNumber = value[2]
        phoneNumber = value[3]

    if Phone == phoneNumber and IC == icNumber:
        print("Succesfully login!")
    else:
        print("Login failed. Please try again.")
        login_func()

def signup_func(): #signup page
    print("Please key in the following details:")
    name = input('Name: Capital Letters \n').title().strip()
    age = input('Age: \n').strip()
    ic= input('IC: No "-" E.g 0123456789 \n').strip()
    phone = input('Phone number: E.g 6017890382 \n').strip()
    postcode=int(input('Postcode: \n'))
    address=input('Address: \n').strip()

    myCursor.execute("INSERT INTO userdata (user_name , user_age, ic_number, phone_number, post_code, home_address) VALUES (?, ?, ?, ?, ?, ?)", (name, age, ic, phone, postcode, address))
    connection.commit()
    print("New user successfully registered!")

def welcome_func(): #so users have the option to login or register
    print('What would you like to do?')
    option = int(input("1- Login \n2- Register: \n"))
    if option == 1:
        login_func()
    elif option == 2:
        signup_func()
    else:
        welcome_func()


########################################################### FUNCTIONS FOR WELCOMEPAGE #########################################################################

########################################################### WELCOMEPAGE #########################################################################

print('Hello user!')
print('Welcome to MySejahtera!\n')


#welcome_func()

########################################################### WELCOMEPAGE #########################################################################
######### Hannah's part ##########

########## Hakeem's part ##########
#hakeem, please type out your code here
########## Hakeem's part ##########

########## Nabilah's part ##########
print("Hello world")
########## Nabilah's part ##########

########## ajwad's part ###########    
def createVaccinationCenter():
    #in table vaccinationCenters (name text, postcode int, address text, capacityHour int, capacityDay int)
    
    VCNAME = input("Please enter the vaccination center name: ").title().strip()
    VCPOSTCODE = int(input("Please enter the postcode: "))
    VCADDRESS = input("Please enter the address: ")
    VCCAPACITYHOUR = int(input("Please enter the capacity per hour: "))
    VCCAPACITYDAY = int(input("Please enter the capacity per day: "))

    #insert data to database
    myCursor.execute("INSERT INTO vaccinationCenters (name, postcode, address, capacityHour, capacityDay), (?, ?, ?, ?, ?)", (VCNAME, VCPOSTCODE, VCADDRESS, VCCAPACITYHOUR, VCCAPACITYDAY))
    connection.commit()

    print("Vaccination center has been registered succesfully")
    whatToDo()

def updateUserInfo():
    def editUser():
        pass

    def deleteUser():
        pass

    def updateOption():
        print("1- edit user information \n2- delete user information")
        userInput = int(input())

        if userInput == 1:
            editUser()
        elif userInput == 2:
            deleteUser()
        else:
            print("Please enter a valid option.")
            updateOption()

def assignAppointment():
    pass

def sortList():
    pass

def whatToDo():
    print("Welcome admin! What do you want to do? \n1- create vaccination center \n2- update user information \n3- assign appointment for user \n4- sort list of users \n5- logout \n6- exit")
    userInput = int(input())

    if userInput == 1:
        createVaccinationCenter()
    elif userInput == 2:
        updateUserInfo()
    elif userInput == 3:
        assignAppointment()
    elif userInput == 4:
        sortList()
    elif userInput == 5:
        welcome_func()
    elif userInput == 6:
        exit()
    else:
        print("Please enter a valid option.")
        whatToDo()

########## ajwad's part ########### 

welcome_func()



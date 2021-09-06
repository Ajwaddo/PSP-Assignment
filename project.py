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


welcome_func()

########################################################### WELCOMEPAGE #########################################################################
######### Hannah's part ##########

########## Hakeem's part ##########
#hakeem, please type out your code here
########## Hakeem's part ##########

########## Nabilah's part ##########
#nabilah, please type out your code here
########## Nabilah's part ##########

########## ajwad's part ###########    
#ajwad, please type out your code here
########## ajwad's part ########### 



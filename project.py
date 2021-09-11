# *********************************************************
# Program: YOUR_FILENAME.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TT0?
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211103139 | HANNAH SOFEA BINTI ROSLEE | 1211103139@student.mmu.edu.my | +60123616790
# Member_2: ID | NAME | EMAIL | PHONES
# Member_3: 1211103138 | NURUL NABILAH BINTI MOHD NOOR HAKIM | 1211103138@student.mmu.edu.my | +60132027946
# Member_4: 1211103128 | MUHAMMAD AJWAD BIN MOHAMAD A'SIM | 1211103128@student.mmu.edu.my | +601154261979
# *********************************************************
# Task Distribution
# Member_1:Account sign up & login authentication
# Member_2:Menu and result display
# Member_3:Public user update information & view appointment
# Member_4:Administrator assign appointment,create vaccination center & generate list
# *********************************************************

import sqlite3
from sqlite3.dbapi2 import SQLITE_SELECT, connect
connection = sqlite3.connect('user.db')
myCursor = connection.cursor()
#in user.db, it has one table(userdata) that contains(user_name text, user_age int, ic_number text, phone_number text, post_code int, home_address text, user_type text, q1 text, q2 text, q3 text, q4 text, q5 text, q6 text, priority int, vaccination_date text, vaccination_time text, vaccination_venue text) 

########## Hannah's part ##########
########################################################### FUNCTIONS FOR WELCOMEPAGE #########################################################################

def login_func(userOrAdmin): #login page
    def userLogin(): #for user to log in
        print("-"*50)
        Phone = input('Enter your phone number: \n').strip()
        IC = input('Enter your IC number: \n').strip()
        
        retrieved_user_data = myCursor.execute("SELECT * FROM userdata WHERE ic_number= :IC", {'IC':IC}) #to search the ic number inputted == with in the database or not

        for value in retrieved_user_data:
            icNumber = value[2]
            phoneNumber = value[3]
            userType = value[6]
        try:
            if Phone == phoneNumber and IC == icNumber and userType == "user":
                print("Succesfully login!")
                userPage(IC)
            else:
                if input("Login failed. Try again(Y), Back(N) ").capitalize() == "Y":
                    login_func(userOrAdmin)
                else:
                    welcome_func()
        except UnboundLocalError: #catch execption when ic number and phone number not found in database
            if input("Login failed. Try again(Y). Back(N) ").capitalize() == "Y":
                login_func(userOrAdmin)
            else:
                welcome_func()

    def adminLogin(): #for admin to login
        print("-"*50)
        Phone = input('Enter your phone number: \n').strip()
        IC = input('Enter your IC number: \n').strip()
        
        retrieved_user_data = myCursor.execute("SELECT * FROM userdata WHERE ic_number= :IC", {'IC':IC}) #to search the ic number inputted == with in the database or not

        for value in retrieved_user_data:
            icNumber = value[2]
            phoneNumber = value[3]
            userType = value[6]
        try:
            if Phone == phoneNumber and IC == icNumber and userType == "admin":
                print("Succesfully login!")
                adminPage()
            else:
                if input("Login failed. Try again(Y). Back(N) ").capitalize() == "Y":
                    login_func(userOrAdmin)
                else:
                    welcome_func()
        except UnboundLocalError: #catch execption when ic number and phone number not found in database
            if input("Login failed. Try again(Y). Back(N) ").capitalize() == "Y":
                login_func(userOrAdmin)
            else:
                welcome_func()

    if userOrAdmin == 1:
        userLogin()
    else:
        adminLogin()

def signup_func(userOrAdmin): #signup page
    def userSignup(): #sign up for user
        print("Please key in the following details:")
        name = input('Name: Capital Letters \n').title().strip()
        age = input('Age: \n').strip()
        ic= input('IC: No "-" E.g 0123456789 \n').strip()
        phone = input('Phone number: E.g 6017890382 \n').strip()
        postcode=int(input('Postcode: \n'))
        address=input('Address: \n').strip()
        userType = "user"

        myCursor.execute("INSERT INTO userdata (user_name , user_age, ic_number, phone_number, post_code, home_address, user_type) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, age, ic, phone, postcode, address, userType))
        connection.commit()
        print("New user successfully registered!")
        userPage(ic)

    def adminSignup(): #sign up for admin
        print("Please key in the following details:")
        name = input('Name: Capital Letters \n').title().strip()
        age = input('Age: \n').strip()
        ic= input('IC: No "-" E.g 0123456789 \n').strip()
        phone = input('Phone number: E.g 6017890382 \n').strip()
        postcode=int(input('Postcode: \n'))
        address=input('Address: \n').strip()
        userType = "admin"

        myCursor.execute("INSERT INTO userdata (user_name , user_age, ic_number, phone_number, post_code, home_address, user_type) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, age, ic, phone, postcode, address, userType))
        connection.commit()
        print("New admin successfully registered!")
        adminPage()

    if userOrAdmin == 1:
        userSignup()
    else:
        adminSignup()

def welcome_func(): #so users have the option whether to login or register
    print("-"*50)
    try:
        userOrAdmin = int(input("Are you a user or an admin? \n1- User \n2- Admin \n")) #to determine whether user or admin use this program
    except ValueError:
        print("Please enter a valid option.")
        welcome_func()

    print('What would you like to do?')
    try:
        option = int(input("1- Login \n2- Register \n3- Exit: \n"))
        if option == 1:
            login_func(userOrAdmin)
        elif option == 2:
            signup_func(userOrAdmin)
        elif option == 3:
            exit()
        else:
            welcome_func()
    except ValueError:
        print("Please enter a valid option.")
        welcome_func()
    

########################################################### FUNCTIONS FOR WELCOMEPAGE #########################################################################

########################################################### WELCOMEPAGE #########################################################################

print('Hello user!')
print('Welcome to MySejahtera!\n')

########################################################### WELCOMEPAGE #########################################################################
######### Hannah's part ##########



########## Hakeem's part ##########
def userPage(ic): #user will be redirected here after signed up / logged in hakeem can view anything

    print('_'*50)
    print('1. COVID-19 Status \n2. View appoinment \n3. Logout') 
    print('_'*50)

    def AppointmentPreferred(): #to ask people what day they prefer to get vaccinated/ where/ when
        preferredDate = input("What date do you prefer to have your appointment? (dd/mm): ").strip()
        preferredLocation = input("Where do you prefer to get vaccinated? ")
    n = int(input())
    if n == 1:
        pass
    elif n == 2: 
        ViewAppointment(ic)
    elif n == 3:
        welcome_func()
    else:
        print("Please enter a valid option.")
        userPage(ic)
    
########## Hakeem's part ##########

########## Nabilah's part ##########

def Vaccination():   
    print('1. Are you interested to take the COVID-19 vaccine? ')
    q1 = input('("Y/N"):')

    print('2. Are you have any illnesses? ')
    q2 = input('("Y/N")?: ')

    if q2 == "Y" or q2 == "y":
        e = input("Enter your illnesses: ")
    
    elif q2 == "N" or q2 == "n":
        pass

    print('3. Are you registered with the department of Social Welfare Malaysia as a Disabled Person (OKU)? ')
    q3 = input('("Y/N"):')

    print('4. Are you currently pregnant?' )
    q4 = input('("Y/N"):')

    print('5. Are you currently breastfeeding?' )
    q5 = input('("Y/N"):')
        
    print('6. Are you a frontliner?' )
    q6 = input('("Y/N:")?: ')

    print('7. What is your occupation?' )
    print('1- Health-care worker')
    print('2- Community Services; Energy, Food, Transportation')
    print('3- Workers')
    print('4- Students')
    print('5- Else')
    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1','2','3','4','5']:
            break
        if userChoice == '1':
            print('Health-care worker() ')
        elif userChoice == '2':
            print('Community Services; Energy, Food, Transportation() ')
        elif userChoice == '3':
            print('Workers() ')
        elif userChoice == '4':
            print('Students() ')
        elif userChoice == '5':
            occupation = input("Enter your Occupation: ")
            print(f'{occupation} ')
        else:
            pass

    print('-'*50)
    print('1. Submit')
    print('2. Cancel')
    n = int(input())

    priority = 0 #to declare variable priority
    #to check whether the user answer Y / N
    if n == 1:
        priority = 0
        if q1 == "Y" or q1 == "y":
            priority += 1
        if q2 == "Y" or q2 == "y":
            priority += 1
        if q3 == "Y" or q3 == "y":
            priority += 1
        if q4 == "Y" or q4 == "y":
            priority += 1
        if q5 == "Y" or q5 == "y":
            priority += 1
        if q6 == "Y" or q6 == "y":
            priority += 1
        if userChoice in ['1','2','3','4','5']:
            priority += 1

        if priority>3:
            print(f'You are ELIGIBLE for vaccine')
            print('View Appoinment')
        elif priority<3:
            print(f'You are NOT ELIGIBLE for vaccine yet')
        else:
            print(f'You are NOT ELIGIBLE for vaccine yet')
        
        main()
    elif n == 2:
        main()

def COVID19Status():
    print('1. Are you exhibiting 2 or more symptoms as listed below? ')
    print('- Fever')
    print('- Chills')
    print('- Shivering') 
    print('- Body ache')
    print('- Headache')
    print('- Sore throat')
    print('- Nausea or vomiting')
    print('- Diarrhea') 
    print('- Fatigue')
    print('- Runny nose or nasal congestion')
    q1 = input('("Y/N")?: ').strip().capitalize()

    print('2. Besides the above, are you exhibiting any of the symptoms listed below? ')
    print('- Cough')
    print('- Difficulty breathing')
    print('- Loss of smell')
    print('- Loss of taste')
    q2 = input('("Y/N:")?: ').strip().capitalize()

    print('3. Are you immunocompromised or have health conditions such as; ')
    print('- Chronic Respiratory Diseases')
    print('- Chronic Kidney Diseases')
    print('- Cardiovascular Diseases')
    print('- Chronic Lung Diseases')
    print('- Hyper-tension')
    print('- Diabetes')
    print('- Obesity')
    print('- Asthma')
    print('- Cancer')
    q3 = input('("Y/N")?: ').strip().capitalize()

    q4 = input('4. Have you attended any event/areas associated with known COCID-19 cluster("Y/N:")?: ').strip().capitalize()
    q5 = input('5. Have you travelled to any country outside Malaysia within 14 days before onset of symptoms("Y/N")?: ').strip().capitalize()
    q6 = input('6. Have you had close contact to confirmed or suspected case of COVID-19 within 14 days before onset of illness("Y/N")?: ').strip().capitalize()
    q7 = input('7. Are you a MOH COVID-19 volunteer in the last 14 days("Y/N")?: ').strip().capitalize()

    print('-'*50)
    print('1. Submit')
    print('2. Cancel')
    n = int(input())

    priority = 0 #to declare variable priority
        #to check whether the user answer Y / N
    if n == 1:
        priority = 0

        if q1 == "Y" or q1 == "y":
            priority += 1
        if q2 == "Y" or q2 == "y":
            priority += 1
        if q3 == "Y" or q3 == "y":
            priority += 1
        if q4 == "Y" or q4 == "y":
            priority += 1
        if q5 == "Y" or q5 == "y":
            priority += 1
        if q6 == "Y" or q6 == "y":
            priority += 1
        if q7 == "Y" or q7 == "y":
            priority += 1

        if priority>3:
            print(f'Covid-19 Risk Status = High Risk')
            print('You are UNDER QUARANTINE')
        elif priority<3:
            print(f'Covid-19 Risk Status = Low Risk')
            print('You are NORMAL')
        else:
            print(f'Covid-19 Risk Status = High Risk')
            print('You are UNDER QUARANTINE')
        main()
    elif n == 2:
        main()
    else:
        print("Please enter a valid input.")

def ViewAppointment(ic): #to view appointment
    for value in myCursor.execute("SELECT vaccination_date, vaccination_time, vaccination_venue FROM userdata WHERE ic_number = :IC", {'IC':ic}):
            vaccinationDate = value[0]
            vaccinationTime = value[1]
            vaccinationVenue = value[2]
    
    if vaccinationDate != None and vaccinationTime != None and vaccinationVenue != None:
        print(f"Your appointment is on {vaccinationDate}, {vaccinationTime} at the {vaccinationVenue}.")
    else:
        print("You have no appointment yet.")
        userPage(ic)

def main():
    print('_'*50)
    print("PUBLIC USER UPDATE INFORMATION")
    print('_'*50)
    print() 
    print('1. Vaccination')
    print('2. COVID-19 Status') 
    print('3. View appoinment')
    print('4. Log out')
    print('_'*50)
    print()
        
    userChoice = input("Choose An Option: ")
    if userChoice == '1':
        Vaccination()
    elif userChoice == '2':
        COVID19Status()
    elif userChoice == '3': 
        pass
        #ViewAppointment(ic)
    else:
        welcome_func()
    main()
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
    myCursor.execute("INSERT INTO vaccinationCenters (name, postcode, address, capacityHour, capacityDay) VALUES (?, ?, ?, ?, ?)", (VCNAME, VCPOSTCODE, VCADDRESS, VCCAPACITYHOUR, VCCAPACITYDAY))
    connection.commit()

    print("Vaccination center has been registered succesfully")
    adminPage()
  
def deleteUser():
    IC = input("Please enter the user IC: ")
    myCursor.execute("DELETE FROM userdata WHERE ic_number = :IC", {'IC':IC})
    connection.commit()
    print("User deleted.")

def assignAppointment():
    print("User without appointment date: ")
    for user in myCursor.execute("SELECT rowid, * FROM userdata"): #search user without appointment
        if user[15] == None:
            print(f'ID: {user[0]} | IC number: {user[2]} | Appointment date: {user[15]}')
    print("-"*50)

    selectUser = int(input("Enter the user ID: "))
    for val in myCursor.execute("SELECT rowid, * FROM vaccinationCenters"):
        print(f"ID: {val[0]} | Vaccination center name: {val[1]} | Address: {val[3]} | Postcode: {val[2]} | Capacity per hour: {val[4]} | Capacity per day: {val[5]}", )
    
    
def sortList():
    #choose to sort list by what
    def exit():
                exitToAdminMenu = input("Press Q to close and go to admin menu: ").capitalize()
                if exitToAdminMenu == "Q":
                    adminPage()
                else:
                    exit()

    print("How you want to sort the list? \n1- name \n2- age \n3- ic number \n4- phone number \n5- postcode \n6- priority")
    userInput = int(input())

    if userInput == 1:
        for val in myCursor.execute("SELECT * FROM userdata ORDER BY user_name"):
            print(val)
            exit()    
    elif userInput == 2:
        for val in myCursor.execute("SELECT * FROM userdata ORDER BY user_age"):
            print(val)
        exit()        
    elif userInput == 3:
        for val in myCursor.execute("SELECT * FROM userdata ORDER BY ic_number"):
            print(val)
        exit()         
    elif userInput == 4:
        for val in myCursor.execute("SELECT * FROM userdata ORDER BY phone_number"):
            print(val)
        exit()          
    elif userInput == 5:
        for val in myCursor.execute("SELECT * FROM userdata ORDER BY post_code"):
            print(val)
        exit()
    elif userInput == 6:
        for val in myCursor.execute("SELECT * FROM userdata ORDER BY priority"):
            print(val)
        exit() 
    else:
        print("Please enter a valid option.")
        sortList()

def adminPage():
    print("Welcome admin! What do you want to do? \n1- create vaccination center \n2- update user information \n3- assign appointment for user \n4- sort list of users \n5- logout \n6- exit")
    userInput = int(input())

    if userInput == 1:
        createVaccinationCenter()
    elif userInput == 2:
        deleteUser()
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
        adminPage()

########## ajwad's part ########### 
main()



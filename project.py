# *********************************************************
# Program: YOUR_FILENAME.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TT0?
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211103139 | HANNAH SOFEA BINTI ROSLEE | 1211103139@student.mmu.edu.my | +60123616790
# Member_2: 1211103830| HAKEEM BIN AMINUDIN | 1211103830@student.mmu.edu.my | +601121380773
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
from operator import itemgetter
connection = sqlite3.connect('user.db')
myCursor = connection.cursor()
#in user.db, it has one table(userdata) that contains(rowid int, user_name text, user_age int, ic_number text, phone_number text, post_code int, home_address text, user_type text, q1_1 text, q1_2 text, q1_3 text, q1_4 text, q1_5 text, q1_6 text, q1_7 text, q2_1 text, q2_2 text, q2_3 text, q2_4 text, q2_5 text, q2_6 text, q2_7 text, priority int, vaccination_date text, vaccination_time text, vaccination_venue text) 

myCursor.execute("SELECT rowid, * FROM userdata") #query all data from userdata table
listUser = myCursor.fetchall() #store all data in database into a tuple list listUser

myCursor.execute("SELECT rowid, * FROM vaccinationCenters") #query all data from vaccinationCenters table
listVaccinationCenters = myCursor.fetchall() #store all data in database into a tuple list listVaccinationCenters

########## Hannah's part ##########
########################################################### FUNCTIONS FOR WELCOMEPAGE #########################################################################

def login_func(): #login page

    #define function
    def loginFailed(): #what to do when login failed
        if input("Login failed. Try again(Y), Back(N) ").capitalize() == "Y":
            login_func()
        else:
            welcome_func()

    def userLogin(): #for user to log in
        print("-"*50)
        Phone = input('Enter your phone number: \n').strip()
        IC = input('Enter your IC number: \n').strip()
        
        for value in listUser: #iterate through listUser and assign variable to some values in it
            icNumber = value[3]
            phoneNumber = value[4]
            userType = value[7]

        while True:
            if Phone == phoneNumber and IC == icNumber and userType == "user":
                print("Succesfully login!")
                mainMenu(IC) #go to user main menu
            else:
                loginFailed()
        
    def adminLogin(): #for admin to login
        print("-"*50)
        Phone = input('Enter your phone number: \n').strip()
        IC = input('Enter your IC number: \n').strip()
        
        for value in listUser: #iterate through listUser and assign variable to some values in it
            icNumber = value[3]
            phoneNumber = value[4]
            userType = value[7]

        while True:
            if Phone == phoneNumber and IC == icNumber and userType == "admin":
                print("Succesfully login!")
                mainMenu(IC) #go to user main menu
            else:
                loginFailed()
    
    #determine user/admin
    userInput = int(input("Are you a, \n1- User \n2- Admin \n"))
    if userInput == 1:
        userLogin()
    elif userInput == 2:
        adminLogin()

def signup_func(): #signup page

    #define function
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
        mainMenu(ic)

    def adminSignup(): #sign up for user
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
    
    #determine user/admin
    userInput = int(input("Are you a, \n1- User \n2- Admin \n"))
    if userInput == 1:
        userSignup()
    elif userInput == 2:
        adminSignup()

def welcome_func(): #so users have the option whether to login or register
    print("-"*50)
    print('What would you like to do?')

    while True:
        option = int(input("1- Login \n2- Register \n3- Exit: \n"))
        if option == 1:
            login_func()
        elif option == 2:
            signup_func()
        elif option == 3:
            exit()
        else:
            print("Please enter a valid option.")
            welcome_func()
 
########################################################### FUNCTIONS FOR WELCOMEPAGE #########################################################################

########################################################### WELCOMEPAGE #########################################################################

#call functions
print('Hello user!')
print('Welcome to MySejahtera!\n')

########################################################### WELCOMEPAGE #########################################################################
######### Hannah's part ##########

########## Hakeem's part ##########
def rsvp(ic): #questions about appointment confirmation
    print("-"*50)
    def preferredTimeDate(ic):
        for value in listUser:
            IC = value[3] 
            Name = value[1] 
            if IC == ic:
                print(f"Hello, {Name}!")
                if value[25] == None:
                    print("sorry you don't have appointment date yet.")
                    if value[27]: #to check whether user have appointment or not
                        print("please wait for your appointment.")
                        print("_"*50)
                        mainMenu(ic)
                    else:
                        print("-"*50)
                        preferredTimeDate(ic)
                else: #if already has an appointment
                    print(f"date = {value[24]} | time = {value[25]} | venue = {value[26]}")
                    print('1. Are you confirm to take Covid-19 vaccine at the date given')
                    q1 = input('("Y/N"):')

                    if q1 == "Y" or q1 == "y":
                        print ("Thank you for your answer")
                        #store user input
                        myCursor.execute("UPDATE userdata SET rsvp:q1 WHERE ic_number")
                    elif q1 == "N" or q1 == "n":
                         #update table
                        newVaccinationDate = None
                        newVaccinationTime = None
                        newVaccinationVenue = None
                        
                        myCursor.execute("UPDATE userdata SET rsvp vaccination_date = none, vaccination_time = none, vaccination_venue = none WHERE ic_number = : IC", {'IC':IC})
                        connection.commit()

def editUser(ic): #to edit user data
    # update userdata 
    icNumber = input("Please enter IC: ")
    newName = input("Please enter your new name: ")
    newAddress = input("Please enter your new address: ")
    newPostcode = input("please enter your new post code: ")
    newNumber = input("please enter your new number: ")
    

    if len(newName) == 0: # if no input from user
        pass
    else:
        myCursor.execute(""" UPDATE userdata SET user_name = :newName WHERE ic_number = :icNumber""", {'icNumber':icNumber,'newName':newName})
        connection.commit()

    if len(newAddress) == 0:
        pass
    else:
        myCursor.execute("UPDATE userdata SET home_address = :newAddress WHERE ic_number = :icNumber " , {'icNumber':icNumber, 'newAddress':newAddress})
        connection.commit()

    if len(newPostcode) == 0:
        pass
    else:
        myCursor.execute("UPDATE userdata SET post_code = :newPostcode WHERE ic_number = :icNumber " , {'icNumber':icNumber, 'newAddress':newPostcode})
        connection.commit()

    if len(newNumber) == 0:
        pass
    else:
        myCursor.execute("UPDATE userdata SET phone_number = :newNumber WHERE ic_number = :icNumber " , {'icNumber':icNumber, 'newNumber':newNumber})
        connection.commit()
    
    print("Your data has been update succesfully")


########## Hakeem's part ##########

########## Nabilah's part ##########

def mainMenu(ic): #user main menu
    print('_'*50)
    print("PUBLIC USER UPDATE INFORMATION")
    print('_'*50)
    print('1. Vaccination \n2. COVID-19 Status \n3. View appoinment \n4. Log out')
    print('_'*50)
    print()
        
    userChoice = input("Choose An Option: ")
    if userChoice == '1':
        Vaccination(ic)
    elif userChoice == '2':
        COVID19Status(ic)
    elif userChoice == '3': 
        ViewAppointment(ic)
    elif userChoice == '4':
        welcome_func() #go back to welcome page
    else:
        mainMenu(ic)

def Vaccination(ic): #questions about vaccination
    print('1. Are you interested to take the COVID-19 vaccine? ')
    q1 = input('("Y/N"):')

    print('2. Are you have any illnesses? ')
    q2 = input('("Y/N")?: ')

    if q2 == "Y" or q2 == "y":
        q2 = input("Enter your illnesses: ")
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
    print('1- Health-care worker \n2- Community Services; Energy, Food, Transportation \n3- Workers \n4- Students \n5- Else')
    
    while True:
        userChoice = input("Choose An Option: ")
        
        if userChoice == '1':
            occupation = 'Health-care worker'
            break
        elif userChoice == '2':
            occupation = 'Community Services; Energy, Food, Transportation'
            break
        elif userChoice == '3':
            occupation = 'Workers'
            break
        elif userChoice == '4':
            occupation = 'Students'
            break
        elif userChoice == '5':
            occupation = input("Enter your Occupation: ")
            break
        else:
            print("Please enter a valid option.")

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
        if userChoice == 1: 
            priority += 2
        elif userChoice == 2:
            priority += 1
        elif userChoice == 3:
            priority += 1
        elif userChoice == 4:
            priority += 2
        elif priority == 5:
            priority += 1

        if priority>3:
            print(f'You are ELIGIBLE for vaccine')
            print('View Appoinment')
        elif priority<3:
            print(f'You are NOT ELIGIBLE for vaccine yet')
        else:
            print(f'You are NOT ELIGIBLE for vaccine yet')

        mainMenu(ic)
    else:
        mainMenu(ic)

def COVID19Status(ic): #questions about health status
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
    q1 = input('("Y/N")?: ')

    print('2. Besides the above, are you exhibiting any of the symptoms listed below? ')
    print('- Cough')
    print('- Difficulty breathing')
    print('- Loss of smell')
    print('- Loss of taste')
    q2 = input('("Y/N:")?: ')

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
    q3 = input('("Y/N")?: ')

    q4 = input('4. Have you attended any event/areas associated with known COCID-19 cluster("Y/N:")?: ')
    q5 = input('5. Have you travelled to any country outside Malaysia within 14 days before onset of symptoms("Y/N")?: ')
    q6 = input('6. Have you had close contact to confirmed or suspected case of COVID-19 within 14 days before onset of illness("Y/N")?: ')
    q7 = input('7. Are you a MOH COVID-19 volunteer in the last 14 days("Y/N")?: ')

    print('-'*50)
    print('1. Submit')
    print('2. Cancel')
    n = int(input())

    priority = 0 #to declare variable priority
        #to check whether the user answer Y / N
    if n == 1:
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

        mainMenu(ic)
    elif n == 2:
        mainMenu(ic)
    else:
        print("Please enter a valid input.")
        COVID19Status(ic)

def ViewAppointment(ic): #to view appointment
    
    for value in listUser: #iterate through listUser and assign variable to some values in it
            vaccinationDate = value[24]
            vaccinationTime = value[25]
            vaccinationVenue = value[26]
    
    if vaccinationDate != None: #check whether user has appointment or not
        print(f"Your appointment is on {vaccinationDate}, {vaccinationTime} at the {vaccinationVenue}.")
    else:
        print("You have no appointment yet.")
        mainMenu(ic)

########## Nabilah's part ##########

########## ajwad's part ###########   

def createVaccinationCenter(): #to create vaccination center
    #in table vaccinationCenters has (rowid int, name text, postcode int, address text, capacityHour int, capacityDay int)
    
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
  
def deleteUser(): #to delete user
    IC = input("Please enter the user IC: ")
    myCursor.execute("DELETE FROM userdata WHERE ic_number = :IC", {'IC':IC})
    connection.commit()
    print("User deleted.")
    adminPage()

def assignAppointment(): #to assign appointment
    print("User without appointment date: ")

    for value in listUser: #show user without appointment
        userID = value[0]
        username = value[1]
        appointmentDate = value[24]
        print(f"userID: {userID} | username: {username} | appointment date: {appointmentDate}")
    print("-"*50)
    for value in listVaccinationCenters: #show vaccination center
        centerID = value[0]
        print(value)

    selectUser = int(input("Enter the user ID: "))
    newAppointmentDate = input("Please enter the appointment date (dd/mm/yyyy): ")
    newAppointmentTime = input("Please enter the appointment time (24-hour): ")
    newAppointmentVenue = int(input("Please enter the vaccination center name: "))

    #update into database
    myCursor.execute("UPDATE userdata SET appointmentDate = :newAppointmentDate, appointmentTime = :newAppointmentTime, appointmentVenue = :newAppointmentVenue WHERE rowid = :selectUser", 
    {'newAppointmentDate':newAppointmentDate, 'newAppointmentTime':newAppointmentTime, 'newAppointmentVenue':newAppointmentVenue, 'selectUser':selectUser})
    connection.commit()
    print("user appointment updated!")
      
def sortList(): #sort list of users
    #choose to sort list by what
    def exit():
        while True:
            exitToAdminMenu = input("Press Q to go to admin menu: ").capitalize()
            if exitToAdminMenu == "Q":
                adminPage()
                break
            else:
                exit()

    print("How you want to sort the list? \n1- name \n2- age \n3- ic number \n4- phone number \n5- postcode \n6- priority")
    userInput = int(input())
    
    if userInput == 1: #sort by name
        print(sorted(listUser,key=lambda listUser: listUser[1]))
        exit()
    elif userInput == 2: #sort by age
        print(sorted(listUser,key=lambda listUser: listUser[2]))
        exit()        
    elif userInput == 3: #sort by ic number
        print(sorted(listUser,key=lambda listUser: listUser[3]))
        exit()          
    elif userInput == 4: #sort by phone number
        print(sorted(listUser,key=lambda listUser: listUser[4]))
        exit()          
    elif userInput == 5: #sort by postcode
        print(sorted(listUser,key=lambda listUser: listUser[5]))
        exit() 
    elif userInput == 6: #sort by priority
        print(sorted(listUser,key=lambda listUser: listUser[23]))
        exit() 
    else:
        print("Please enter a valid option.")
        sortList()

def adminPage(): #admin main menu
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
welcome_func()

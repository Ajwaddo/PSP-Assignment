#whattodo
#add priority1, priority2, priority - done
#sum up priority1 and priority2 as priority
#only show priority when sorting user/assign appointment
#add preferred time, date into database - done
#fix database - done
#make list display as table(sort)
#make auto assignment of appointment
#put preferred date,time when want to assign appointment

#problems
#cannot add priority in Vaccination() and COVID19Status()


# *********************************************************
# Program: YOUR_FILENAME.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TT0?
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211103139 | HANNAH SOFEA BINTI ROSLEE | 1211103139@student.mmu.edu.my | +60123616790
# Member_2: ID | NAME | EMAIL | PHONES
# Member_3: 1211103183 | NURUL NABILAH BINTI MOHD NOOR HAKIM | 1211103183@student.mmu.edu.my | +60132027946
# Member_4: 1211103128 | MUHAMMAD AJWAD BIN MOHAMAD A'SIM | 1211103128@student.mmu.edu.my | +601154261979
# *********************************************************
# Task Distribution
# Member_1:Account sign up & login authentication
# Member_2:Menu and result display
# Member_3:Public user update information & view appointment
# Member_4:Administrator assign appointment,create vaccination center & generate list
# *********************************************************

import sqlite3
import math
import datetime
from operator import itemgetter, pos
connection = sqlite3.connect('user.db')
myCursor = connection.cursor()
def createDatabase():
    myCursor.execute("DROP TABLE userdata")
    print("table dropped")
    myCursor.execute("CREATE TABLE userdata (user_name text, user_age text, ic_number text, phone_number text, post_code text, home_address text, q1_1 text, q1_2 text, q1_3 text, q1_4 text, q1_5 text, q1_6 text, q1_7 text, q2_1 text, q2_2 text, q2_3 text, q2_4 text, q2_5 text, q2_6 text, q2_7 text, priority text, priority1 text, priority2 text, vaccination_date text, vaccination_time text, vaccination_venue text, preferred_time text, preferred_date text, rsvp text, state text)")
#in user.db, it has one table(userdata) that contains(0rowid int, 1user_name text, 2user_age text, 3ic_number text, 4phone_number text, 5post_code text, 6home_address text, 7q1_1 text, 8q1_2 text, 9q1_3 text, 10q1_4 text, 11q1_5 text, 12q1_6 text, 13q1_7 text, 14q2_1 text, 15q2_2 text, 16q2_3 text, 17q2_4 text, 18q2_5 text, 19q2_6 text, 20q2_7 text, 21priority text, 22priority1 text, 23priority2 text, 24vaccination_date text, 25vaccination_time text, 26vaccination_venue text, 27preferred_time text, 28preffered_date text, 29rsvp text, 30state text) 

myCursor.execute("SELECT rowid, * FROM userdata") #query all data from userdata table
listUser = myCursor.fetchall() #store all data in database into a tuple in list listUser

myCursor.execute("SELECT rowid, * FROM vaccinationCenters") #query all data from vaccinationCenters table
listVaccinationCenters = myCursor.fetchall() #store all data in database into a tuple in list listVaccinationCenters

########## Hannah's part ##########
########################################################### FUNCTIONS FOR WELCOMEPAGE #########################################################################

def login_func(): #login page
    #define function
    def userLogin(): #for user to log in
        print("-"*50)
        IC = input('Enter your IC number: \n').strip()
        
        while True:
            for value in listUser: #iterate through listUser and assign variable to some values in it
                icNumber = value[3]
                if IC == icNumber:
                    print("Succesfully login!")
                    rsvp(IC) #go to user main menu
                    break
                else:
                    if input("Login failed. Try again(Y), Back(N) ").capitalize() == "Y":
                        login_func()
                        break
                    else:
                        welcome_func()
                        break

    #determine user/admin
    userInput = int(input("Are you a, \n1- User \n2- Admin \n"))
    if userInput == 1:
        userLogin()
    elif userInput == 2:
        adminPage()

def signup_func(): #signup page
    print("Please key in the following details:")
    name = input('Name: Capital Letters \n').title().strip()
    age = input('Age: \n').strip()
    ic= input('IC: No "-" E.g 0123456789 \n').strip()
    phone = input('Phone number: E.g 6017890382 \n').strip()
    postcode=int(input('Postcode: \n'))
    address=input('Address: \n').strip()
    state = input('State: \n').strip()
    

    myCursor.execute("INSERT INTO userdata (user_name , user_age, ic_number, phone_number, post_code, home_address, state) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, age, ic, phone, postcode, address, state))
    connection.commit()
    print("New user successfully registered!")
    rsvp(ic)
    
def welcome_func(): #so users have the option whether to login or register
    print("-"*50)
    print('What would you like to do?')

    while True:
        option = int(input("1- Login \n2- Register \n3- Exit: \n"))
        if option == 1:
            login_func()
            break
        elif option == 2:
            signup_func()
            break
        elif option == 3:
            exit()
        else:
            print("Please enter a valid option.")
            welcome_func()
 
########################################################### FUNCTIONS FOR WELCOMEPAGE #########################################################################
######### Hannah's part ##########

########## Hakeem's part ##########
def rsvp(ic): #questions about appointment confirmation
    print("-"*50)
    def preferredTimeDate(ic):
        preferredDate = input("What is your preffered date to take your vaccine? (dd/mm/yyyy): ")
        preferredTime = input("What is your preferred time to take your vacine? (24-hour): ")

        #update in database
        myCursor.execute("UPDATE userdata SET preferred_time = :preferredTime, preferred_date = :preferredDate WHERE ic_number = :ic", 
        {'preferredTime':preferredTime, 'preferredDate':preferredDate, 'ic':ic})
        connection.commit()
        print("Preferred time and date updated. Please wait for your appointment.")
        print("_"*50)
        mainMenu(ic)
    for value in listUser: # for loop to iterate through listUser
        IC = value[3] # assign value on index to IC
        NAME = value[1] # assign value on index to IC
        if IC == ic: # compare whether IC(from database) is equal to ic(inputted by user during login/signup) 
            print(f"Hello, {NAME}!") # string formatting
            if value[25] == None: # check if user has vaccination time(appointment) or not
                print("Sorry, you don't have appointment date yet.")
                # if value[27]: #check whether user have preferred date or not yet
                #     print("Please wait for your appointment.")
                #     print("_"*50)
                #     mainMenu(ic)
                # else:
                #     print("_"*50)
                #     preferredTimeDate(ic)
            else: # if user already has an appointment
                print(f"date = {value[24]} | time = {value[25]} | venue = {value[26]}") # print vaccination date, time, venue
                print('1. Are you confirm to take the COVID-19 vaccine at the date given') # function rsvp
                q1 = input('("Y/N"):') # confirmation for appointment

                if q1 == "Y" or q1 == "n":
                    print("Thank you for your answer")
                    # store user input
                    myCursor.execute("UPDATE userdata SET rsvp = :q1 WHERE ic_number = :ic", {'q1':q1, 'ic':IC}) # update changes into database
                    connection.commit() # save changes into database
                    
                elif q1 == "N" or q1 == "n":
                    #preferredTimeDate(ic)
                    newDate = None
                    newTime = None
                    newVenue = None

                    # update in the database
                    myCursor.execute("UPDATE userdata SET rsvp = :q1, vaccination_date = :newDate, vaccination_Time = :newTime, vaccination_venue = :newVenue WHERE ic_number = :ic", {'q1':q1, 'newDate':newDate, 'newTime':newTime, 'newVenue':newVenue, 'ic':IC})
                    connection.commit()
                mainMenu(ic)
                

def editUser(ic):
    newPhoneNumber = input("Please enter your new phone number: ")
    newName = input("Please enter your new name: ")
    
    if len(newPhoneNumber) != 0: 
        myCursor.execute("UPDATE userdata SET phone_number = :newPhoneNumber", {'newPhoneNumber':newPhoneNumber})
        connection.commit()
    if len(newName) != 0: # user inputted something in newName
        myCursor.execute("UPDATE userdata SET user_name = :newName", {'newName':newName})
        connection.commit()
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
    
    global priority1
    priority1 = 0 #to declare variable priority2

    #to check whether the user answer Y / N total priority = 7
    if n == 1:
        if q1 == "Y" or q1 == "y":
            priority1 += 1
        if q2 == "Y" or q2 == "y":
            priority1 += 1
        if q3 == "Y" or q3 == "y":
            priority1 += 1
        if q4 == "Y" or q4 == "y":
            priority1 += 1
        if q5 == "Y" or q5 == "y":
            priority1 += 1
        if q6 == "Y" or q6 == "y":
            priority1 += 1
        if userChoice == 1: 
            priority1 += 1
        elif userChoice == 2:
            priority1 += 1
        elif userChoice == 3:
            priority1 += 1
        elif userChoice == 4:
            priority1 += 1
        elif userChoice == 5:
            priority1 += 1

        #update priority and questions into database
        myCursor.execute("UPDATE userdata SET priority1 = :priority, q1_1 = :q1_1, q1_2 = :q1_2, q1_3 = :q1_3, q1_4 = :q1_4, q1_5 = :q1_5, q1_6 = :q1_6, q1_7 = :q1_7 WHERE ic_number = :ic_number",
        {'priority':priority1, 'q1_1':q1, 'q1_2':q2, 'q1_3':q3, 'q1_4':q4, 'q1_5':q5, 'q1_6':q6, 'q1_7':occupation, 'ic_number':ic})
        connection.commit()
        print("Successfully updated!")
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

    global priority2
    priority2 = 0 #to declare variable priority2

        #to check whether the user answer Y / N
    if n == 1:
        if q1 == "Y" or q1 == "y":
            priority2 += 1
        if q2 == "Y" or q2 == "y":
            priority2 += 1
        if q3 == "Y" or q3 == "y":
            priority2 += 1
        if q4 == "Y" or q4 == "y":
            priority2 += 1
        if q5 == "Y" or q5 == "y":
            priority2 += 1
        if q6 == "Y" or q6 == "y":
            priority2 += 1
        if q7 == "Y" or q7 == "y":
            priority2 += 1

        #update priority and questions into database
        myCursor.execute("UPDATE userdata SET priority2 = :priority, q2_1 = :q2_1, q2_2 = :q2_2, q2_3 = :q2_3, q2_4 = :q2_4, q2_5 = :q2_5, q2_6 = :q2_6, q2_7 = :q2_7 WHERE ic_number = :ic_number",
        {'priority':priority2, 'q2_1':q1, 'q2_2':q2, 'q2_3':q3, 'q2_4':q4, 'q2_5':q5, 'q2_6':q6, 'q2_7':q7, 'ic_number':ic})
        connection.commit()
        print("Successfully updated!")
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

def createVaccinationCenter(): #to create vaccination center --done
    #in table vaccinationCenters has (rowid int, name text, postcode int, address text, capacityHour int, capacityDay int, state text)
    
    VCNAME = input("Please enter the vaccination center name: ").title().strip()
    VCPOSTCODE = int(input("Please enter the postcode: "))
    VCADDRESS = input("Please enter the address: ")
    VCSTATE = input("Please enter the state: ")
    VCCAPACITYHOUR = int(input("Please enter the capacity per hour: "))
    VCCAPACITYDAY = int(input("Please enter the capacity per day: "))

    #insert data to database
    myCursor.execute("INSERT INTO vaccinationCenters (name, postcode, address, capacityHour, capacityDay, state) VALUES (?, ?, ?, ?, ?, ?)", (VCNAME, VCPOSTCODE, VCADDRESS, VCCAPACITYHOUR, VCCAPACITYDAY, VCSTATE))
    connection.commit()

    print("Vaccination center has been registered succesfully")
    adminPage()

def list_vaccination_centers():
    for center in listVaccinationCenters:
        for user in listUser:
            if center[1] == user[26]:
                print(user[0], user[1], user[2], user[3], user[4], user[5], user[6])
        print()

def deleteUser(): #to delete user
    IC = input("Please enter the user IC: ")
    myCursor.execute("DELETE FROM userdata WHERE ic_number = :IC", {'IC':IC})
    connection.commit()
    print("User deleted.")
    adminPage()

def assignAppointment(hour, day, month, year, userID, vaccCenter): # done
    myCursor.execute("UPDATE userdata SET vaccination_date = :vaccDate, vaccination_venue = :vaccVenue, vaccination_time = :vaccTime WHERE rowid = :rowid", 
    {'vaccDate':f"{day}/{month}/{year}", 'vaccVenue':vaccCenter, 'vaccTime':f"{hour}:00", 'rowid':userID})
    connection.commit()

def secAutoAssign():
    date_function = datetime.datetime.now()
    time_function = datetime.datetime.now()
    day = int(date_function.strftime('%d'))
    month = int(date_function.strftime('%m'))
    year = int(date_function.strftime('%Y'))
    hour = int(time_function.strftime('%H'))
    
    # store user info yang tak dapat appointment lagi & yang dah dapat appointment dah dalam list
    userWithoutAppointment = [[i[0], i[30]] for i in listUser if i[24] == None] # userID, userState
    userWithAppointment = [[i[0], i[26], i[24][0:2], i[24][3:5], i[25][0:2]] for i in listUser if i[24] != None] # userID, userVenue, userDay, userMonth, userTime

    # check day free or not
    for i in listVaccinationCenters:
        userPerDay = 0
        userPerHour = 0
        vaccCenter = i[1]
        maxPerDay = i[5]
        maxPerHour = i[4]
        vaccState = i[6]

        myCursor.execute("SELECT rowid FROM userdata WHERE vaccination_venue = :vaccVenue and vaccination_date = :vaccDate", {'vaccVenue':vaccCenter, 'vaccDate':f"{day}/{month}/{year}"})
        userPerDay += len(myCursor.fetchall())

        if userPerDay < maxPerDay and day < 28:
            myCursor.execute("SELECT rowid FROM userdata WHERE vaccination_venue = :vaccVenue and vaccination_date = :vaccDate and vaccination_time = :vaccTime", {'vaccVenue':vaccCenter, 'vaccDate':f"{day}/{month}/{year}", 'vaccTime':f"{hour}:00"})
            userThisHour = myCursor.fetchall()
            userPerHour += (len(userThisHour))

            if userPerHour < maxPerHour and hour >= 8 and hour<=18:
                for i in userWithoutAppointment:
                    userID = i[0]
                    userState = i[1]
                    
                    if vaccState == userState:
                        assignAppointment(hour, day, month, year, userID, vaccCenter)
            else:
                hour += 1
        else:
            day += 1
      
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
        for value in myCursor.execute("SELECT * FROM userdata ORDER BY user_name"):
            print(value)
        exit()
    elif userInput == 2: #sort by age
        for value in myCursor.execute("SELECT * FROM userdata ORDER BY user_age"):
            print(value)
        exit()        
    elif userInput == 3: #sort by ic number
        for value in myCursor.execute("SELECT * FROM userdata ORDER BY ic_number"):
            print(value)
        exit()         
    elif userInput == 4: #sort by phone number
        for value in myCursor.execute("SELECT * FROM userdata ORDER BY phone_number"):
            print(value)
        exit()         
    # elif userInput == 5: #sort by postcode
    #     for value in myCursor.execute("SELECT * FROM userdata ORDER BY post_code"):
    #         print(value)
    #     exit()
    elif userInput == 6: #sort by priority
        for value in myCursor.execute("SELECT * FROM userdata ORDER BY priority"):
            print(value)
        exit() 
    else:
        print("Please enter a valid option.")
        sortList()

def userCategory(): #low, medium, high
    while True:
        userInput = int(input("Please choose the category \n1- low risk \n2- medium risk \n3- high risk \n"))
        for value in listUser: #get user data
            userPriority = value[21]
        if userInput == 1:
            if userPriority == 1 or userPriority == 2:
                print(value)
        elif userInput == 2:
            if userPriority == 3 or userPriority == 4:
                print(value)
        elif userInput == 3:
            if userPriority == 5 or userPriority == 6:
                print(value)
        else:
            print("Please enter a valid input.")
            break

def adminPage(): #admin main menu --done
    print("Welcome admin! What do you want to do? \n1- create vaccination center \n2- update user information \n3- assign appointment for user \n4- sort list of users \n5- view user appointments \n6- logout \n7- exit")
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
        list_vaccination_centers()
    elif userInput == 6:
        welcome_func()
    elif userInput == 7:
        exit()
    else:
        print("Please enter a valid option.")
        adminPage()

########## ajwad's part ########### 

########################################################### WELCOMEPAGE #########################################################################

#call functions
print('Hello user!')
print('Welcome to MySejahtera!\n')
#welcome_func()
#assignAppointment()
#autoAssign()
#adminPage()
#createDatabase()
secAutoAssign()
#signup_func()
#login_func()
#createVaccinationCenter()
#rsvp("020732130394")
#mainMenu("030102020131")
########################################################### WELCOMEPAGE #########################################################################


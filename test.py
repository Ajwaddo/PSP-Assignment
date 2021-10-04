import sqlite3
from operator import itemgetter
connection = sqlite3.connect('user.db')
myCursor = connection.cursor()
def createDatabase():
    myCursor.execute("DROP TABLE userdata")
    print("table dropped")
    myCursor.execute("CREATE TABLE userdata (user_name text, user_age text, ic_number text, phone_number text, post_code text, home_address text, q1_1 text, q1_2 text, q1_3 text, q1_4 text, q1_5 text, q1_6 text, q1_7 text, q2_1 text, q2_2 text, q2_3 text, q2_4 text, q2_5 text, q2_6 text, q2_7 text, priority text, priority1 text, priority2 text, vaccination_date text, vaccination_time text, vaccination_venue text, preferred_time text, preferred_date text, rsvp text)")
#in user.db, it has one table(userdata) that contains(0rowid int, 1user_name text, 2user_age text, 3ic_number text, 4phone_number text, 5post_code text, 6home_address text, 7q1_1 text, 8q1_2 text, 9q1_3 text, 10q1_4 text, 11q1_5 text, 12q1_6 text, 13q1_7 text, 14q2_1 text, 15q2_2 text, 16q2_3 text, 17q2_4 text, 18q2_5 text, 19q2_6 text, 20q2_7 text, 21priority text, 22priority1 text, 23priority2 text, 24vaccination_date text, 25vaccination_time text, 26vaccination_venue text, 27preferred_time text, 28preffered_date text, 29rsvp text) 

myCursor.execute("SELECT rowid, * FROM userdata") #query all data from userdata table
listUser = myCursor.fetchall() #store all data in database into a tuple list listUser

def longest():
    longest_name = 0
    for user in listUser:
        if len(user[1]) > longest_name:
            longest_name = len(user[1])
    return longest_name

head = "name"+" "*(longest()-len("name"))+" | age | ic number | phone number | postcode | priority | date | time | venue | rsvp |"
print(head)
print("-"*len(head))
for element in listUser:
    print(element[1] + " "*(longest()-len(element[1])) +f" | {element[2]} | {element[3]} | {element[4]} | {element[5]} | {element[21]} | {element[24]} | {element[25]} | {element[26]} | {element[29]}" ) 
    
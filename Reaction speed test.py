#Took use of W3 schools tutorial if you're interested: https://www.w3schools.com/python/python_mysql_getstarted.asp
import time
import random
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "host",
    user = "user",
    password = "password",
    database = "Reactions"
)

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()

name = input("Welcome to the Reaction Speed Test,\nPlease type your username and press the enter key when you are ready to start ")
loop = True
nameLoop = True
reactionLoop = True
testLoop = True
retryLoop = True

while nameLoop: #While True
    corrctName = input("\n"+name+", Are you happy with your username? (Y/N) ")
    corrctName = corrctName.lower()
    corrctName = corrctName[:1]
    
    if corrctName == "y":
        nameLoop = False
    
    elif corrctName == "n":
        name = input("\nPlease retype your username and press the enter key when you are ready to start ")
        #time.sleep(5)

print("\nGET READY!\n\nThere will be a countdown and then you must press enter when prompted.")
while testLoop:
    time.sleep(5)
    print("\nYou will be prompted by the word 'NOW'.")
    time.sleep(3)
    print("\n3")
    time.sleep(1)
    print("\n2")
    time.sleep(1)
    print("\n1")
    time.sleep(2)
    time.sleep(random.randint(1,4))
    start = time.time()
    test = input("NOW!")
    while reactionLoop:
        if test == "":
            reactionLoop = False
    end = time.time()
    reaction = end-start
    if reaction < (0.01):
        print("\n\nDo not press enter until prompted!")
        time.sleep(5)
        retryLoop = True
        while retryLoop:
            ask = input("\nWould you like to try again? (Y/N) ")
            ask = ask.lower()
            ask = ask[:1]
           
            if ask == "y":
                retryLoop = False
               
            elif ask == "n":
                print("\nThank you for playing")
                time.sleep(5)
                testLoop = False
                retryLoop = False
           
    else:
        print("\n\nWell Done "+name+", your reaction speed was "+str(reaction)+"!")
        testLoop = False

cursor.execute("INSERT INTO Reactions (Username,Reaction_Speed) VALUES ('"+name+"','"+str(reaction)+"');")
# Commit the changes to the database
mydb.commit()
# Close the cursor and the connection
cursor.close()
mydb.close()
time.sleep(1)
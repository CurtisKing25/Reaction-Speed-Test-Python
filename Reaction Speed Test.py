import time
import random
go = input("Welcome to the Reaction Speed Test,\nPress the enter key when you are ready to start")
loop = True
loop2 = True
loop3 = True
loop4 = True

while loop: #While True
    if go == "":
        loop = False
    else: go = input("Press the enter key when you are ready to start.")
print("\nGET READY!\n\nThere will be a countdown and then you must press enter when prompted.")
while loop3:
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
    while loop2:
        if test == "":
            loop2 = False
    end = time.time()
    reaction = end-start
    if reaction < (0.01):
        print("\n\nDo not press enter until prompted!")
        time.sleep(5)
        loop4 = True
        while loop4:
            ask = input("\nWould you like to try again? (Y/N) ")
            ask = ask.lower()
            ask = ask[:1]
           
            if ask == "y":
                loop4 = False
               
            elif ask == "n":
                print("\nThank you for playing")
                time.sleep(5)
                loop3 = False
                loop4 = False
           
    else:
        print("\n\nYour reaction speed was",reaction,"!")
        loop3 = False
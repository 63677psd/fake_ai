import getpass
import time
import choices
from setup import *

# prints opening text
for i in openingTxt:
    print(i)
    time.sleep(0.5)
print()

# log in
while not loggedIn and run:
    username = input("Username: ")
    if username == "exit": exit()
    password = getpass.getpass("Password: ")
    if db.loginCheck(username, password):
        loggedIn = True
        print("You are logged in.")
        print()
    else:
        print("Username or Password is incorrect.")
        print()
    time.sleep(1)

# main loop
while run:
    x = input(">>> ")
    if x == "exit":
        exit()
    else:
        choices.execute(x)
    

exit()

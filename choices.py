import re
import webbrowser
from datetime import datetime
from db import Db
import getpass
import subprocess

# actions    
def showTime():
    print(datetime.now().strftime("%m/%d/%Y %I:%M %p"))
def openWebpage(x):
    webbrowser.get( \
    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(str(x))
def createAccount():
    db = Db()
    if db.createAccount(input("Username: "), getpass.getpass("Password: ")):
        print("Account created.")
    else:
        print("There was an error.")
    db.exit()
def deleteAccount():
    db = Db()
    if db.deleteAccount(input("Username: ")):
        print("Account deleted.")
    else:
        print("There was an error.")
    db.exit()
def listUsers():
    db = Db()
    users = db.listUsers()
    for i in users:
        print(i)
def start(x):
    subprocess.call(("start", x), shell=True)
def echo(x):
    print(x)
        

def check(x, action, *args, **kwargs):
    if x:
        action(*args, **kwargs)
        return True
    else:
        return False

# test every regex
def execute(s):
    try:
        result = re.findall(r'.*\s+(.*\.(?:com|org|net|gov).*)', s)
        if check(result, openWebpage, result[0].strip(".")): return True
    except IndexError:
        pass

    result = re.findall(r'[Tt]ime', s)
    if check(result, showTime): return True

    result = re.findall(r'(?:[Cc]reate|[Aa]dd).+(?:[Uu]ser|[Aa]ccount)', s)
    if check(result, createAccount): return True

    result = re.findall(r'[Dd]el.*\s+(?:[Uu]ser|[Aa]ccount)', s)
    if check(result, deleteAccount): return True

    result = re.findall(r'(?:[Ll]ist|[Ss]how).*(?:[Uu]ser|[Aa]ccount)', s)
    if check(result, listUsers): return True

    result = re.findall(r'(?:[Oo]pen|[Ss]tart|[Rr]un) (.*)', s)
    if check(result, start, result): return True

    try:
        result = re.findall(r'(?:[Ee]cho|[Pp]rint) (.*)', s)
        if check(result, echo, result[0]): return True
    except IndexError:
        pass
    

    return False
    


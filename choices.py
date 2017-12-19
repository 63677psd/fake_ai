import re
import webbrowser
from datetime import datetime
from db import Db
import getpass

# actions    
def showTime():
    print(datetime.now().strftime("%m/%d/%Y %I:%M %p"))
def openWebpage(x):
    webbrowser.get( \
    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(str(x))
def createAccount():
    db = Db()
    db.createAccount(input("Username: "), getpass.getpass("Password: "))
    db.exit()

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

    result = re.findall(r'(?:[Cc]reate|[Aa]dd)\s(?:[Uu]ser|[Aa]ccount)', s)
    if check(result, createAccount): return True

    return False
    

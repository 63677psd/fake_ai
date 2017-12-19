from db import Db
import sys

db = Db()

db.setupDb()

try:
    u = sys.argv[1]
    p = sys.argv[2]
    db.createAccount(u,p)
except IndexError:
    pass

db.exit()

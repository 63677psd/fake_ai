import sqlite3
import base64

class Db:
    def __init__(self):
        self.db = sqlite3.connect("fake_ai.db")
        self.cursor = self.db.cursor()
    def exit(self):
        self.db.close()
    def setupDb(self):
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.cursor.execute("""
        CREATE TABLE users(
            username varchar(255),
            password varchar(255)
        )
        """)
        self.db.commit()
    def loginCheck(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE " \
                            "username=? AND password=?", (username, self._encode(password)))
        if self.cursor.fetchone() is None:
            return False
        else:
            return True
    def createAccount(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE " \
                            "username=?", (username,))
        if self.cursor.fetchone() is not None:
            return False
        else:
            self.cursor.execute("""
                INSERT INTO users(username, password)
                VALUES(?,?)
            """, (username, self._encode(password)))
            self.db.commit()
            return True
    def _encode(self, s):
        s = str(s)
        s = s.encode("utf-8")
        return base64.b64encode(s)
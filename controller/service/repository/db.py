import mysql.connector
import os


class Database:
    def __init__(self):
        self.mydb = self.init_db()

    def init_db(self):
        mydb = mysql.connector.connect(
          host=os.getenv("DATABASE_HOST"),
          user="root",
          password="mata",
          database="la_kantina"
        )

        return mydb

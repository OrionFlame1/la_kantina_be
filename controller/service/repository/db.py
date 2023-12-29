import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def init_db():
    mydb = mysql.connector.connect(
      host=os.getenv("DATABASE_HOST"),
      user="root",
      password="mata",
      database="la_kantina"
    )

    return mydb

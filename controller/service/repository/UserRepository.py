from .db import Database
import hashlib


class UserRepository:
    def validateLogin(data):
        db = Database().mydb
        cursor = db.cursor()
        result = {}

        cursor.execute(f"SELECT * FROM accounts WHERE email = '{data['email']}'")
        try:
            result["foundUser"] = cursor.fetchone()[0]
        except:
            result["foundUser"] = False

        encrypted_password = hashlib.sha256(data['password'].encode()).hexdigest()
        cursor.execute(f"SELECT * FROM accounts WHERE email = '{data['email']}' AND password = '{encrypted_password}'")
        result["password"] = True if cursor.fetchone() else False

        cursor.close()
        db.close()
        return result

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

    def createAccount(data):
        db = Database().mydb
        cursor = db.cursor()
        encrypted_password = hashlib.sha256(data['password'].encode()).hexdigest()
        cursor.execute(f"INSERT INTO accounts SET "
                       f"name = '{data['name']}', "
                       f"email = '{data['email']}', "
                       f"password = '{encrypted_password}', "
                       f"points = 0")
        db.commit()
        cursor.execute(f"SELECT id, email FROM accounts WHERE email = '{data['email']}'")
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return {'error': 0, 'message': "Account created successfully", 'id': result[0], 'email': result[1]}


    def confirmAccount(account_id):
        db = Database().mydb
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM accounts WHERE id = {account_id}")
        if not cursor.fetchone():
            cursor.close()
            db.close()
            return {'error': 1, 'message': "Account not found"}
        cursor.execute(f"UPDATE accounts SET type = 'customer' WHERE id = {account_id}")
        db.commit()
        cursor.close()
        db.close()
        return {'error': 0, 'message': "Account confirmed successfully"}

    # validate an account based on if the email already exists in the database, or the username already exists in the database

    def validateRegister(data):
        db = Database().mydb
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM accounts WHERE email = '{data['email']}'")
        result = cursor.fetchall()
        if len(result) > 0:
            cursor.close()
            db.close()
            return {'error': 1, 'message': "Email already exists"}
        cursor.execute(f"SELECT * FROM accounts WHERE name = '{data['name']}'")
        result = cursor.fetchall()
        if len(result) > 0:
            cursor.close()
            db.close()
            return {'error': 2, 'message': "Username already exists"}
        cursor.close()
        db.close()
        return {'error': 0, 'message': "Account validated successfully"}

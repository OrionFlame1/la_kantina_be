from controller.service.repository import db
from hashlib import sha256

db = db.init_db()

def getRoleByUserId(userId):
    cursor = db.cursor()
    cursor.execute(f'SELECT type FROM accounts WHERE id = {userId}')
    result = cursor.fetchone()[0]

    cursor.close()
    return result

def userToJSON(result):
    return {
        "id": result[0],
        "name": result[1],
        "email": result[2],
        "type": result[4],
        "points": result[5]
    }

def hasAdmin(userId):
    userRole = getRoleByUserId(userId)
    return userRole == 'admin'

def validateLoginData(email, password):
    cursor = db.cursor()
    encrypted_password = sha256(password.encode()).hexdigest()
    cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, encrypted_password))
    user = cursor.fetchone()
    cursor.close()

    return user
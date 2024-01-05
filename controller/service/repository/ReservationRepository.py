# from db import Database
from .db import Database

class ReservationRepository:
    def getReservationsToday():
        db = Database().mydb
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM reservations WHERE date = CURDATE()")

        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result
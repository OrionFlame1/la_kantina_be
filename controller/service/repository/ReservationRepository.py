# from db import Database
from models.Reservation import Reservation
from .db import Database


class ReservationRepository:
    def getReservationsToday():
        db = Database().mydb
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM reservations WHERE DATE(start_at) = CURDATE() ORDER BY created_at ASC")
        result = cursor.fetchall()
        print(result)

        result = [Reservation(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).toJSON() for row in result]
        cursor.close()
        db.close()
        return result

    def getAllReservations():
        db = Database().mydb
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM reservations ORDER BY created_at ASC")
        result = cursor.fetchall()
        result = [Reservation(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).toJSON() for row in result]
        cursor.close()
        db.close()
        return result

    def createReservation(data):
        db = Database().mydb
        cursor = db.cursor()

        # first check if there is already a reservation made in the same date and time for a specific table
        cursor.execute(f"SELECT * FROM reservations WHERE "
                       f"( "
                       f"   ( start_at <= CAST('{data['start_at']}' AS DATETIME) "  # reservation in the limits of other reservation
                       f"   AND end_at >= CAST('{data['end_at']}' AS DATETIME) "
                       f") OR "
                       f"   ( start_at >= CAST('{data['start_at']}' AS DATETIME) "  # reservation conflict with other reservation's upper limit
                       f"   AND start_at <= CAST('{data['end_at']}' AS DATETIME) "
                       f") OR "
                       f"   ( end_at >= CAST('{data['start_at']}' AS DATETIME) "  # reservation conflict with other reservation's lower limit
                       f"   AND end_at <= CAST('{data['end_at']}' AS DATETIME) ) "
                       f") AND table_id = {data['table_id']}")  # check for that specific table
        result = cursor.fetchall()
        if len(result) > 0:
            cursor.close()
            db.close()
            return {'error': 1, 'message': "There is already a reservation made in the same date and time"}
        cursor.execute(f"INSERT INTO reservations SET "
                       f"account_id = '{data['user_id']}', "
                       f"table_id = '{data['table_id']}', "
                       f"start_at = '{data['start_at']}', "
                       f"end_at = '{data['end_at']}', "
                       f"status = 'pending', "
                       f"created_at = NOW()")
        db.commit()
        cursor.execute(
            f"SELECT email FROM accounts a JOIN reservations r WHERE a.id = r.account_id AND r.id = {cursor.lastrowid}")
        email = cursor.fetchone()[0]
        cursor.close()
        db.close()
        return {'error': 0, 'message': "Reservation created successfully", 'reservation_id': cursor.lastrowid,
                'email': email}

    def findReservationById(id):  # also sends the email of the user
        db = Database().mydb
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM reservations WHERE id = {id}")
        result = cursor.fetchone()
        if result:
            cursor.execute(
                f"SELECT email FROM accounts a JOIN reservations r WHERE a.id = r.account_id AND r.id = {id}")
            email = cursor.fetchone()[0]
            cursor.close()
            db.close()
            return {'error': 0, 'reservation': result, 'email': email}
        cursor.close()
        db.close()
        return result

    def updateReservationStatus(reservation_id, status):
        db = Database().mydb
        cursor = db.cursor()
        cursor.execute(f"UPDATE reservations SET status = '{status}' WHERE id = {reservation_id}")
        db.commit()
        cursor.close()
        db.close()
        return {'error': 0, 'message': "Reservation updated successfully"}

    def getReservationsByUser(id):
        db = Database().mydb
        cursor = db.cursor()
        try:
            cursor.execute(f"SELECT * FROM reservations WHERE account_id = {id} AND end_at > now()")
            result = cursor.fetchall()
            return [Reservation(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in result]
        except:
            return []

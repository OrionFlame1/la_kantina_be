# from db import Database
from .db import Database

class ReservationRepository:
    def getReservationsToday():
        db = Database().mydb
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM reservations ORDER BY created_at ASC")
        result = cursor.fetchall()
        result = [dict(zip([key[0] for key in cursor.description], row)) for row in result]
        cursor.close()
        db.close()
        return result

    def createReservation(data):
        db = Database().mydb
        cursor = db.cursor()
        # first check if there is already a reservation made in the same date and time
        sql = f"SELECT * FROM reservations WHERE (start_at < CAST('{data['end_at']}' AS DATETIME) OR end_at > CAST('{data['start_at']}' AS DATETIME)) AND table_id = {data['table_id']}"
        print(sql)
        cursor.execute(f"SELECT * FROM reservations WHERE "
                       f"(start_at < CAST('{data['end_at']}' AS DATETIME) OR "
                       f"end_at > CAST('{data['start_at']}' AS DATETIME)) AND "
                       f"table_id = {data['table_id']}")
        result = cursor.fetchall()
        if len(result) > 0:
            cursor.close()
            db.close()
            return {'error': 1, 'message': "There is already a reservation made in the same date and time"}
        # cursor.execute(f"INSERT INTO reservations SET "
        #                f"account_id = '{data['user_id']}', "
        #                f"table_id = '{data['table_id']}', "
        #                f"start_at = '{data['start_at']}', "
        #                f"end_at = '{data['end_at']}', "
        #                f"status = 'pending', "
        #                f"created_at = NOW()")
        # db.commit()
        cursor.close()
        db.close()
        return {'error': 0, 'message': "Reservation created successfully"}
from .db import Database


class TableRepository:

    def getAllTablesWithReservationsOnDate(date, isAdmin):
        db = Database().mydb
        cursor = db.cursor()
        try:
            cursor.execute(f"SELECT * FROM tables tab LEFT JOIN (SELECT * FROM reservations WHERE UNIX_TIMESTAMP(STR_TO_DATE('{date}', '%Y-%m-%d_%H:%i:%s')) < UNIX_TIMESTAMP(reservations.end_at) AND status <> 'cancelled' AND status <> 'pending' ) res ON tab.id = res.table_id")
            result = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print(e)
            return []

        return result

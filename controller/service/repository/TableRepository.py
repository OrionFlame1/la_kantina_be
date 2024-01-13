from .db import Database


class TableRepository:

    def getAllTablesWithReservationsOnDate(date, isAdmin):
        db = Database().mydb
        cursor = db.cursor()
        try:
            cursor.execute(f"SELECT * FROM tables tab LEFT JOIN (SELECT * FROM reservations WHERE STR_TO_DATE('{date}', '%Y-%m-%d_%H:%i:%s') < reservations.end_at ) res ON tab.id = res.table_id")
            result = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print(e)
            return []

        return result

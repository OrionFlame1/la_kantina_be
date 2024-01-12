from controller.service.repository.TableRepository import TableRepository


class TableService:

    def getTables(date):
        if date is not None:
            resultz = TableRepository.getAllTablesWithReservationsOnDate(date)
            array = []

            for result in resultz:
                if result[4] is None:
                    array.append({
                        "id": result[0],
                        "slots": result[1],
                        "x": result[2],
                        "y": result[3]
                    })
                else:
                    array.append({
                        "id": result[0],
                        "slots": result[1],
                        "x": result[2],
                        "y": result[3],
                        "reservation": {
                            "id": result[4],
                            "userId": result[5],
                            "startDate": result[7],
                            "endDate": result[8],
                            "status": result[9]
                        }
                    })
            return array
        else:
            return []

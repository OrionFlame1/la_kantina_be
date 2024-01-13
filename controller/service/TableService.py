from controller.service.repository.TableRepository import TableRepository


class TableService:

    def getTables(date, isAdmin):
        if date is not None:
            resultz = TableRepository.getAllTablesWithReservationsOnDate(date, isAdmin)
            array = []
            print(resultz)
            for result in resultz:
                if result[4] is None:
                    array.append({
                        "id": result[0],
                        "slots": result[1],
                        "x": result[2],
                        "y": result[3]
                    })
                else:
                    reservations = []
                    i = 4
                    while i <= len(result) - 4:
                        reservations.append({
                            "id": result[i],
                            "userId": result[i+1],
                            "startDate": result[i+2],
                            "endDate": result[i+3],
                            "status": result[i+4]
                        })
                    array.append({
                        "id": result[0],
                        "slots": result[1],
                        "x": result[2],
                        "y": result[3],
                        "reservations": reservations
                    })
            return array
        else:
            return []

from controller.service.repository.TableRepository import TableRepository


class TableService:

    def getTables(date, isAdmin):
        if date is not None:
            resultz = TableRepository.getAllTablesWithReservationsOnDate(date, isAdmin)
            array = []
            for result in resultz:
                if len(array) != 0 and list(filter(lambda elem: elem['id'] == result[0], array)):
                    continue
                if result[4] is None:
                    array.append({
                        "id": result[0],
                        "slots": result[1],
                        "x": result[2],
                        "y": result[3]
                    })
                else:
                    reservations = list(map(reservationToJSONWithoutTableId, filter(lambda elem: elem[0] == result[0], resultz)))
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


def popTablePart(array):
    return [i for i in array if array.index(i) >= 4]

def reservationToJSONWithoutTableId(elem):
    return {
        "id": elem[4],
        "userId": elem[5],
        "startAt": elem[7],
        "endAt": elem[8],
        "status": elem[9]
    }
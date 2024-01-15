from controller.service.repository.TableRepository import TableRepository
from models.Reservation import Reservation
from models.Table import Table


class TableService:

    def getTables(date, isAdmin):
        if date is not None:
            resultz = TableRepository.getAllTablesWithReservationsOnDate(date, isAdmin)
            array = []
            for result in resultz:
                if len(array) != 0 and list(filter(lambda elem: elem['id'] == result[0], array)):
                    continue
                if result[4] is None:
                    array.append(Table(result[0], result[1], result[2], result[3]).toJSON())
                else:
                    reservations = list(map(reservationToJSONWithoutTableId, filter(lambda elem: elem[0] == result[0], resultz)))
                    array.append(Table(result[0], result[1], result[2], result[3], reservations).toJSON())
            return array
        else:
            return []


def popTablePart(array):
    return [i for i in array if array.index(i) >= 4]

def reservationToJSONWithoutTableId(elem):
    return Reservation(elem[4], elem[5], elem[6], elem[7], elem[8], elem[9]).toJSONWithoutTableId()
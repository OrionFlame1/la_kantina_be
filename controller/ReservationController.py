from .service.ReservationService import ReservationService

class ReservationController:
    def getReservations():
        return ReservationService.getReservationsToday()

    def createReservation(data):
        return ReservationService.createReservation(data)

    def cancelReservation(reservation_id):
        return ReservationService.cancelReservation(reservation_id)

    def confirmArrival(reservation_id):
        return ReservationService.confirmArrival(reservation_id)

    def completeReservation(reservation_id):
        return ReservationService.completeReservation(reservation_id)
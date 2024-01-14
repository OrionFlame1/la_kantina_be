from .service.ReservationService import ReservationService

class ReservationController:
    def getReservations():
        return ReservationService.getReservationsToday()

    def createReservation(self, data):
        return ReservationService.createReservation(self, data)

    def confirmReservation(reservation_id):
        return ReservationService.confirmReservation(reservation_id)

    def requestReservationCancellation(self, reservation_id):
        return ReservationService.requestReservationCancellation(self, reservation_id)

    def cancelReservation(reservation_id):
        return ReservationService.cancelReservation(reservation_id)

    def confirmArrival(reservation_id):
        return ReservationService.confirmArrival(reservation_id)

    def completeReservation(reservation_id):
        return ReservationService.completeReservation(reservation_id)
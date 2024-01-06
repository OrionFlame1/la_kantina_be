from .service.ReservationService import ReservationService

class ReservationController:
    def getReservations():
        return ReservationService.getReservationsToday()

    def createReservation(data):
        return ReservationService.createReservation(data)
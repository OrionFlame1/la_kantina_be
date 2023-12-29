from .service.ReservationService import ReservationService

class ReservationController:
    def getReservations(self):
        return ReservationService.getReservationsToday()
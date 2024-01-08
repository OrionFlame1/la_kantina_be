from .repository.ReservationRepository import ReservationRepository

class ReservationService:

        def getReservationsToday():
            return ReservationRepository.getReservationsToday()

        def createReservation(data):
            return ReservationRepository.createReservation(data)

        def cancelReservation(reservation_id):
            return ReservationRepository.updateReservationStatus(reservation_id, status='cancelled')

        def confirmArrival(reservation_id):
            return ReservationRepository.updateReservationStatus(reservation_id, status='confirmed_arrival')

        def completeReservation(reservation_id):
            return ReservationRepository.updateReservationStatus(reservation_id, status='completed')

        # def getReservationsByDate(date):
        #     return ReservationRepository.getReservationsByDate(date)
        #
        # def getReservationsByUser(user_id):
        #     return ReservationRepository.getReservationsByUser(user_id)
        #
        # def getReservationById(id):
        #     return ReservationRepository.getReservationById(id)
        #
        # def createReservation(data):
        #     return ReservationRepository.createReservation(data)
        #
        # def updateReservation(data):
        #     return ReservationRepository.updateReservation(data)
        #
        # def deleteReservation(id):
        #     return ReservationRepository.deleteReservation(id)
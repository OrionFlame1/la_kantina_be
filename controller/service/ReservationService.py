from .repository.ReservationRepository import ReservationRepository
from .MailService import MailService
import os

class ReservationService:

        def getReservationsToday():
            return ReservationRepository.getReservationsToday()

        def createReservation(self, data):
            result = ReservationRepository.createReservation(data)
            if result['error'] == 0:
                url = os.getenv("BASE_URL")
                link = url + "/reservations/confirm/" + str(result['reservation_id'])
                email = result['email']
                print(link)
                mail = MailService(self.app).sendReservationConfirmation(email, link)
                return result
            return result

        def requestReservationCancellation(self, reservation_id):
            result = ReservationRepository.findReservationById(reservation_id)
            if result['error'] == 0:
                url = os.getenv("BASE_URL")
                link = url + "/reservations/cancel/" + str(reservation_id)
                email = result['email']
                mail = MailService(self.app).sendReservationCancellation(email, link)
                return result
            return result

        def confirmReservation(reservation_id):
            return ReservationRepository.updateReservationStatus(reservation_id, status='confirmed')

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
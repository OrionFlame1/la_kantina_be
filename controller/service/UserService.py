from controller.service.repository.UserRepository import UserRepository
from models.Reservation import Reservation
from .MailService import MailService
import os

from .repository.ReservationRepository import ReservationRepository


class UserService:


    def getUserWithReservations(id, sessionUserId):
        user = UserRepository.getUserById(id)
        if user is None:
            return None

        reservations = ReservationRepository.getReservationsByUser(id)
        reservationsJSON = [reservation.toJSONWithoutAccountId() for reservation in reservations]
        result = user.withReservations(reservationsJSON)
        if id == sessionUserId:
            return result.withReservations(reservationsJSON).toJSON()
        else:
            return result.withReservations(reservationsJSON).toJSONWithNameAndReservation()

    def findByEmail(data):
        result = UserRepository.validateLogin(data)
        if not result['foundUser']:
            return "User does not exist!"
        elif not result['password']:
            return "Wrong credentials!"
        else:
            return result['foundUser']
            # return result['foundUser']['id']

    def register(self, data):
        result = UserRepository.validateRegister(data)
        if result['error'] == 0:
            url = os.getenv("BASE_URL")
            result = UserRepository.createAccount(data)
            link = url + "/confirm_account/" + str(result['id'])
            print(link)
            print(result['email'])
            mail = MailService(self.app).sendAccountConfirmation(result['email'], link)
            return result
        else:
            return result['message']

    def confirmAccount(self, account_id):
        result = UserRepository.confirmAccount(account_id)
        if result['error'] == 0:
            return result
        else:
            return result['message']

    def isAdmin(self):
        return UserRepository.isAdmin(self)

from controller.service.repository.UserRepository import UserRepository
from .MailService import MailService
import os

from .repository.ReservationRepository import ReservationRepository


class UserService:


    def getUserWithReservations(id, sessionUserId):
        user = UserRepository.getUserById(id)
        if user is None or len(user) == 0:
            return None

        reservations = ReservationRepository.getReservationsByUser(id)
        reservationsJSON = []
        for reservation in reservations:
            reservationsJSON.append({
                "id": reservation[0],
                "tableId": reservation[2],
                "startDate": reservation[3],
                "endDate": reservation[4],
                "status": reservation[5]
            })

        if id == sessionUserId:
            return {
                "name": user[1],
                "type": user[4],
                "points": user[5],
                "reservations": reservationsJSON
            }
        else:
            return {
                "name": user[1],
                "reservations": reservationsJSON
            }

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

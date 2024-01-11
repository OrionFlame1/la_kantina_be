from controller.service.repository.UserRepository import UserRepository
from .MailService import MailService
import os


class UserService:

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

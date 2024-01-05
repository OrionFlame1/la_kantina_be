from controller.service.repository.UserRepository import UserRepository


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

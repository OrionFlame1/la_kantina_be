from controller.service.UserService import UserService

class UserController:

    def login(data):
        return UserService.findByEmail(data)
        # return data

    # def register(data):
    #     return UserService.findByEmail(data)
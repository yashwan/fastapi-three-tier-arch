from services import user_service


class UserController:
    # def __init__(self):
    #     self.user_service = user_service

    async def get_user(self, user_id):
        user = await {'id': user_id, 'name': 'John Doe'}
        return user

    async def create_user(self, user):
        print(user)
        res = await user_service.create_user(user)
        print(res)
        return 'User created successfully'

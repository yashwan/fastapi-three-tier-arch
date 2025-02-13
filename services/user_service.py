from models.user_model import User
from utils import mongodb


class UserService():
    async def create_user(self, user: User):
        result = await mongodb.db["User"].insert_one(user)
        return result

from app import schemas
from app.models.user import User
from app.core.security import *
import ormar


def no_match_wrapper(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ormar.exceptions.NoMatch:
            return None

    return wrapper


class UserService:
    @no_match_wrapper
    async def get_by_email(self, email):
        user = await User.objects.filter(email=email).get()
        return user

    async def get_by_id(self, id):
        user = await User.objects.filter(id=id).get()
        return user

    async def get_by_username(self, username):
        user = await User.objects.filter(username=username).get()
        return user

    async def create_new_user(self, user_in: schemas.UserCreate, access_lvl:int=None):
        user_data = user_in.dict()
        password = user_data.pop('password')
        user_data['hashed_password'] = get_password_hash(password)
        user = await User.objects.create(**user_data)
        return user

    async def update_user(self, user_id: int, user_update: schemas.UserUpdate):
        user_data = user_update.dict()
        if user_data.get('password', False):
            password = user_data.pop('password')
            user_data['hashed_password'] = get_password_hash(password)
        current_user = await User.objects.get(id=user_id)
        return await current_user.update(**user_data)

    async def authenticate(self, username, password) -> User:
        if username:
            user = await self.get_by_username(username)
        # elif email:
        #    user = await self.get_by_email(email)
        else:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


user_service = UserService()

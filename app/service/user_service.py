from models.user import User as UserModel
from models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService():

    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        return self.db.query(UserModel).all()

    def get_user(self, id: int):
        return self.db.query(UserModel).filter(UserModel.id == id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def create_user(self, user: User):
        hashed_password = pwd_context.hash(user.hashed_password)
        new_user = UserModel(
            name=user.name,
            email=user.email,
            hashed_password=hashed_password
        )
        self.db.add(new_user)
        self.db.commit()
        return

    def update_user(self, id: int, data: User):
        user = self.get_user(id)
        user.name = data.name
        user.email = data.email
        user.hashed_password = pwd_context.hash(data.hashed_password)
        self.db.commit()
        return

    def delete_user(self, id: int):
        user = self.get_user(id)
        self.db.delete(user)
        self.db.commit()
        return

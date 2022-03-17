from flask_login import UserMixin
from app.auth.auth import Auth
class UserModel(UserMixin):
    def __init__(self, userData):
        self.id = userData.username
        self.iduser = userData.id
        self.password = userData.password
        self.email = userData.email
        self.avatar = userData.avatar
        self.isadmin = userData.isadmin
        self.estado = userData.estado
        
    @staticmethod
    def get(username):
        userData = Auth.getUserByUsername(username)
        return UserModel(userData)
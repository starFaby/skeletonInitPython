from app.database.database import *

def getUserByUsername(username):
    return User.query.filter_by(username = username)
from flask import Blueprint
from app.auth.authLogout import AuthLogout
logout= Blueprint('logout', __name__)
logout.route('/logout', methods=['GET'])(AuthLogout.onGetLogout)
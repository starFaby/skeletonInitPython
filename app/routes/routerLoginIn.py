from flask import Blueprint
from app.auth.authLoginIn import AuthLoginIn
loginin= Blueprint('loginin', __name__)
loginin.route('/loginin', methods=['GET'])(AuthLoginIn.onGetLogin)
loginin.route('/loginin', methods=['POST'])(AuthLoginIn.onGetLoginIn)
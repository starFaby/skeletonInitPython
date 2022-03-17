from flask import Blueprint
from app.migrate.migrate import initDB

createdb= Blueprint('createdb', __name__)

createdb.route('/createdb', methods=['GET'])(initDB)

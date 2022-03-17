from flask import Flask
from flask_login import LoginManager
from .config.config import Config
from app.database.database import db, ma
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from app.routes.routerAuth import auth
from app.routes.routerLoginIn import loginin
from app.routes.routerLogout import logout
from app.routes.routerDataBase import createdb
from app.routes.routerCamera import camera
from app.routes.routerVoice import voice
from app.middlewares.authLogin import UserModel

loginManager = LoginManager()
loginManager.loginView = 'auth.authLoginIn'

@loginManager.user_loader
def loadUser(username):
    return UserModel.get(username)

def apprun():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth)
    app.register_blueprint(createdb)
    app.register_blueprint(loginin)
    app.register_blueprint(logout)
    app.register_blueprint(camera)
    app.register_blueprint(voice)
    loginManager.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    bootstrap = Bootstrap(app)
    fa = FontAwesome(app)
    return app




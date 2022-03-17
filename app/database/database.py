from msilib import sequence
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

#---------------------------
#drop database flaskmysql
#create database flaskmysql
#---------------------------

#----------usuario----------
#--------------------------
class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(80), nullable=False)
    nombres = db.Column(db.String(80), nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(250), nullable=True)
    cellphone = db.Column(db.String(100), nullable=False)
    isadmin = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.String(250), nullable=True)
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 

    def onGetSetPassword(self, password):
        self.password = generate_password_hash(password)

    def onGetCheckPassword(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, cedula, nombres, apellidos, username, email, password, cellphone, isadmin, avatar, estado, createdat):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.username = username
        self.email = email
        self.password = password
        self.cellphone = cellphone
        self.isadmin = isadmin
        self.avatar = avatar
        self.estado = estado
        self.createdat = createdat

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','cedula', 'nombres', 'apellidos', 'username', 'email', 'password', 'cellphone', 'isadmin', 'avatar', 'estado', 'createdat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

#---------------------------
#----------Camera IP----------
#--------------------------

class CameraIp(db.Model):
    __tablename__='cameraip'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(80), nullable=False)
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 
    userid = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
    user = db.relationship('User',backref=db.backref('cameraip',lazy=True))


    def __init__(self, ip, descripcion, estado, createdat):
        self.ip = ip
        self.descripcion = descripcion
        self.estado = estado
        self.createdat = createdat

class CameraIpSchema(ma.Schema):
    class Meta:
        fields = ('id','ip', 'descripcion', 'estado', 'createdat')

cameraipSchema = CameraIpSchema()
cameraipSchema = CameraIpSchema(many=True)
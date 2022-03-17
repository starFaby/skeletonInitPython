import sys
from datetime import datetime
from flask import render_template as render, request, jsonify, redirect, url_for
from sqlalchemy.sql.elements import Null
from app.database.database import *

class Auth:

    def onGetAuth():
        return render('auth/auth.html')
    
    def onGetListAuth():
        allTasks = User.query.all()
        result = usersSchema.dump(allTasks)
        return jsonify(result)

    def onGetListOneAuth(self,id):
        pass
 
    def onGetCreateAuth():
        cedula = request.form['txtCedula']
        nombres = request.form['txtNombres']
        apellidos = request.form['txtApellidos']
        username = request.form['txtUsername']
        email = request.form['txtEmail']
        password = request.form['txtPassword']
        cellphone = request.form['txtCelphone']
        isadmin =  False
        avatar = 'https://res.cloudinary.com/dqmbrjl7jfs/image/upload/v1640009274/aux/noimage_b9edhb.jpg'
        estado = request.form['txtEstado']
        createdat = datetime.now().strftime('%x')
        
        newUser = User(cedula, nombres, apellidos, username, email, password, cellphone, isadmin, avatar, estado, createdat)
        newUser.onGetSetPassword(password)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("loginin.onGetLogin"))

    def getUserByUsername(username):
        return User.query.filter_by(username = username).first()

    def onGetUpdateAuth(self):
        pass

    def onGetDeleteAuth(self):
        pass


    
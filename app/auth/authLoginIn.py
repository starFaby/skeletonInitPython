from flask import request, jsonify, flash, render_template as render
from flask_login import login_user, logout_user, login_required
from app.database.database import *
from app.auth.auth import Auth
from app.middlewares.authLogin import UserModel
class AuthLoginIn:
    def onGetLogin():
        return render('auth/login.html')

    def onGetLoginIn():
        txtUsername = request.form['txtUsername']
        txtPassword = request.form['txtPassword']
        user = Auth.getUserByUsername(txtUsername)
        if user is not None:
            if user.onGetCheckPassword(txtPassword): 
                userModel = UserModel(user)
                login_user(userModel)
                flash('logiado correctamente', category='success')
                return render('index.html')
            else:
                flash('Password Incorrecto', category='info')
                return render('auth/login.html')
        else:
            flash('Usuario y password Incorrecto', category='error')
            return render('auth/login.html')
        
        

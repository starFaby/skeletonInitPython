from flask import flash, render_template as render
from flask_login import login_user, logout_user, login_required
class AuthLogout:
        
    def onGetLogout():
        logout_user()
        flash("Cerraste sesion !!", category="info")
        
        return render('index.html')
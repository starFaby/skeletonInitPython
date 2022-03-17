from flask import render_template as render, flash
from app import apprun

app = apprun()

@app.errorhandler(404)
def notfound(error):
    return render('errors/error404.html',error = error)

@app.errorhandler(500)
def internalserveererror(error):
    return render('errors/error500.html')

@app.route('/')
def index():  
    return render('index.html')

if __name__ == '__main__':
    app.run(debug=True)
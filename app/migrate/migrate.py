import sys
from datetime import datetime
from app.database.database import *
def createDB():
    db.drop_all()
    db.create_all()

def initDB():
    createDB()
    admin = User(
        cedula = "1725302705",
        nombres = "edgar fabian",
        apellidos = "estrella guambuguete",
        username = "starfaby",
        email = "star._faby@hotmail.com",
        password = "star123",
        cellphone = "0983856136", 
        isadmin = True,
        avatar = "https://res.cloudinary.com/dqmbrjl7jfs/image/upload/v1638923678/starfaby_uqbwru.jpg",
        estado = 1,
        createdat = datetime.now().strftime('%x')
           
    )
    admin.onGetSetPassword(admin.password)
    db.session.add(admin)
    db.session.commit()  
    return 'base de datos creado existosamente'  
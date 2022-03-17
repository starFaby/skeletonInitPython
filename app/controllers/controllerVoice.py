from flask import request, render_template as render
from app.middlewares.voice import playVoice


class ControllerVoice:
    
    def alertLadron():
        mytext="alejese del lugar"
        cont = 0
        for i in mytext:
            if(i.isalpha()):
                cont +=1
            else:
                break
        
        if cont >= 1:
            print("existe letras")
            playVoice(mytext)
            return render("index.html")
        else:
            print("no esiste letras tonto care....")
            return render("index.html")
 
        
        





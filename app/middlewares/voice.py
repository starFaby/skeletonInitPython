from gtts import gTTS
from playsound import playsound
import os
from app.sound.playSound import playsoundTono 

def playVoice(mytext):
      
   language = 'es'

   myobj = gTTS(text=mytext, lang=language, slow=False)


   myobj.save("app/sound/welcome.mp3")

   playsoundTono()




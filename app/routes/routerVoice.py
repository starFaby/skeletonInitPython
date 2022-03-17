from flask import Blueprint
from flask_cors import cross_origin
from app.controllers.controllerVoice import ControllerVoice
voice= Blueprint('voice', __name__)
voice.route('/voice', methods=['GET'])(ControllerVoice.alertLadron)
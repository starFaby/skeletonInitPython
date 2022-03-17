from flask import Blueprint
from app.controllers.camera import Camera
camera= Blueprint('camera', __name__)
camera.route('/camera', methods=['GET'])(Camera.onGetCamera)
camera.route('/camerastreaming', methods=['GET'])(Camera.streaming_camara)
camera.route('/comenzar_grabacion', methods=['GET'])(Camera.comenzar_grabacion)
camera.route('/detener_grabacion', methods=['GET'])(Camera.detener_grabacion)
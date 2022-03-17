import sys
import cv2
from datetime import datetime
from flask import render_template as render, request, jsonify, redirect, url_for, Response
from app.database.database import *
from app.utils.fechahora import fechahora

#camara = cv2.VideoCapture('rtsp://192.168.1.9:8899/user=admin&password=admin&channel=1&stream=0.sdp?')
camara = cv2.VideoCapture(0)
#camara = cv2.VideoCapture('rtsp://admin:12345scw@192.168.1.7:554/cam/realmonitor?channel=1&subtype=1')
FRAMES_VIDEO = 20.0
RESOLUCION_VIDEO = (640, 480)
UBICACION_FECHA_HORA = (0, 15)
FUENTE_FECHA_Y_HORA = cv2.FONT_HERSHEY_PLAIN
ESCALA_FUENTE = 1
COLOR_FECHA_HORA = (255, 255, 255)
GROSOR_TEXTO = 1
TIPO_LINEA_TEXTO = cv2.LINE_AA
fourcc = cv2.VideoWriter_fourcc(*'XVID')
archivo_video = None
grabando = False
class Camera:
    

    def onGetCamera():
        return render('client/camera.html')

    def agregar_fecha_hora_frame(frame):
        cv2.putText(frame, fechahora.fecha_y_hora(), UBICACION_FECHA_HORA, FUENTE_FECHA_Y_HORA, ESCALA_FUENTE, COLOR_FECHA_HORA, GROSOR_TEXTO, TIPO_LINEA_TEXTO)

    def generador_frames():
        while True:
            ok, imagen = Camera.obtener_frame_camara()
            if not ok:
                break
            else:
                # Regresar la imagen en modo de respuesta HTTP
                yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + imagen + b"\r\n"

    def obtener_frame_camara():
        ok, frame = camara.read()
        if not ok:
            return False, None
        Camera.agregar_fecha_hora_frame(frame)
        # Escribir en el vídeo en caso de que se esté grabando
        if grabando and archivo_video is not None:
            archivo_video.write(frame)
        # Codificar la imagen como JPG
        _, bufer = cv2.imencode(".jpg", frame)
        imagen = bufer.tobytes()

        return True, imagen

    # @app.route("/streaming_camara")
    def streaming_camara():
        return Response(Camera.generador_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

    
    # Cuando toman la foto
    #@app.route("/tomar_foto_descargar")
    def descargar_foto():
        ok, frame = Camera.obtener_frame_camara()
        if not ok:
            abort(500)
            return
        respuesta = Response(frame)
        respuesta.headers["Content-Type"] = "image/jpeg"
        respuesta.headers["Content-Transfer-Encoding"] = "Binary"
        respuesta.headers["Content-Disposition"] = "attachment; filename=\"foto.jpg\""
        return respuesta


    #@app.route("/tomar_foto_guardar")
    def guardar_foto():
        nombre_foto = fechahora.obtener_uuid() + ".jpg"
        ok, frame = camara.read()
        if ok:
            Camera.agregar_fecha_hora_frame(frame)
            cv2.imwrite(nombre_foto, frame)
        return jsonify({
            "ok": ok,
            "nombre_foto": nombre_foto,
        })

    #@app.route("/comenzar_grabacion")
    def comenzar_grabacion():
        global grabando
        global archivo_video
        if grabando and archivo_video:
            return jsonify(False)
        nombre = fechahora.fecha_y_hora_para_nombre_archivo() + ".avi"
        archivo_video = cv2.VideoWriter(
            nombre, fourcc, FRAMES_VIDEO, RESOLUCION_VIDEO)
        grabando = True
        return jsonify(True)


    #@app.route("/detener_grabacion")
    def detener_grabacion():
        global grabando
        global archivo_video
        if not grabando or not archivo_video:
            return jsonify(False)
        grabando = False
        archivo_video.release()
        archivo_video = None
        return jsonify(True)


    #@app.route("/estado_grabacion")
    def estado_grabacion():
        return jsonify(grabando)
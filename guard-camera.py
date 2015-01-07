from logging.handlers import RotatingFileHandler

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import picamera

# app instance
app = Flask(__name__)

# configuration
DEBUG = True
SECRET_KEY = 'development key'
app.config.from_object(__name__)

# logger
#file_handler = RotatingFileHandler('/var/log/lighttpd/pi_camera.log', maxBytes=1024*1024)
#app.logger.addHandler(file_handler)


# controllers
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/shoot")
def shoot():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.capture('static/img.jpg')
    return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

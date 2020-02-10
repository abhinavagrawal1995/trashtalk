import base64
import eventlet
import socketio
from fastai.vision import *
from prediction import magic
import json

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.on('image')
def image(sid, data):
    print("recvd request")
    with open("temp.jpeg", "wb") as fh:
        fh.write(base64.b64decode(data))
    print("written file")

    label = classification_action = magic("temp.jpeg")
    print(label)
    sio.emit('classification', label)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)


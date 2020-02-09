import base64
import eventlet
import socketio
from fastai.vision import *
import json

trained_model_path = "data"
learn = load_learner(trained_model_path)

# sio = socketio.Server(cors_allowed_origins="*")
# app = socketio.WSGIApp(sio, static_files={
#     '/': {'content_type': 'text/html', 'filename': 'index.html'}
# })
#
# @sio.event
# def connect(sid, environ):
#     print('connect ', sid)
#
# @sio.on('image')
# def image(sid, data):
#     with open("temp.jpeg", "wb") as fh:
#         fh.write(base64.b64decode(data))
#
#     with open("temp.jpeg", "rb") as fh:
#         img = open_image(fh)
#         learn.predict(img)
#     sio.emit('def', 'yayyy')
#
# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)

if __name__ == '__main__':
    # eventlet.wsgi.server(eventlet.listen(('', 5001)), app)

    print('start')
    with open("temp.jpeg", "rb") as fh:
        img = open_image(fh)
        pred = learn.predict(img)
        nparr = np.asarray(np.argmax(predictions[0], axis=1))
        print(pred)
        print(nparr)
    print('end')

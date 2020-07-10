import socketio
import eventlet
import time

sio = socketio.Server()

app = socketio.WSGIApp(sio)


@sio.event
def home(sid, data):
    print(data)
    time.sleep(6)
    sio.emit('index', {'age': "20"})


@sio.on('my_message')
def another_event(sid, data):
    print(data)


@sio.event
def connect(sid, environ):
    print('connect')


@sio.event
def disconnect(sid):
    print('disconnect')


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

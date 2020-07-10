import socketio
import time

sio = socketio.Client()


@sio.event
def index(data):
    print(data)
    time.sleep(6)
    sio.emit('my_message', {'height': 188})


@sio.event
def connect():
    sio.emit('home', {'name': 'wzj'})
    print("I'm connected!")


@sio.event
def connect_error():
    print("The connection failed!")


@sio.event
def disconnect():
    print("I'm disconnected!")


sio.connect('http://localhost:5000')

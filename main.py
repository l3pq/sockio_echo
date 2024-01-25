import socketio
sio = socketio.Server(cors_allowed_origins='*')

app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def message(sid, data):
    print('message ', data)
    sio.emit('reply', data, to=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    import eventlet
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

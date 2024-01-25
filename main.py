import socketio

# Tworzenie serwera Socket.IO
sio = socketio.Server(cors_allowed_origins='*')

# Aplikacja WSGI
app = socketio.WSGIApp(sio)

# Obsługa zdarzenia połączenia
@sio.event
def connect(sid, environ):
    print('connect ', sid)

# Obsługa zdarzenia wiadomości
@sio.event
def message(sid, data):
    print('message ', data)
    sio.emit('reply', data, to=sid)

# Obsługa zdarzenia rozłączenia
@sio.event
def disconnect(sid):
    print('disconnect ', sid)

# Uruchomienie serwera
if __name__ == '__main__':
    import eventlet
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

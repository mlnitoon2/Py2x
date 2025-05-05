import socket
import threading

class SFSSession:
    def __init__(self, conn: socket.socket, username: str = None, user_id: int = None, token: str = None):
        self.Connected = True
        self.Username = username
        self.UserId = user_id
        self.Token = token
        self.Connection = conn

    def disconnect(self):
        self.Connected = False
        self.Connection.close()

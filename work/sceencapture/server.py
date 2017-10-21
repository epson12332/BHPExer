from multiprocessing.connection import Listener
from mss import mss
import pickle
import socket


if __name__ == '__main__':
    localIP = socket.gethostbyname(socket.gethostname())
    print("local ip : ",localIP)
    s = Listener((localIP,58888))
    while True:

        conn = s.accept()
        print('Accept a new connection')

        conn.send(pickle.dumps(mss().shot()))
        conn.close()
        print('Closed the connection')

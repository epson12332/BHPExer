from multiprocessing.connection import Client
from mss import mss
import pickle

if __name__ == '__main__':
    host = input("server address: ")

    while True:
        input("get the remote screen? ")
        client = Client((host, 58888))
        img = pickle.loads(client.recv())
        with open("screen.jpeg", "wb") as fp:
            img.save(fp, format = 'jpeg')
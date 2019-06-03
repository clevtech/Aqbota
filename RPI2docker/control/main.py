#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, Aqbota"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"


import lib.arduino_speak as ard
import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

while True:
    try:
        box, light = ard.connect_to()
        break
    except:
        pass


# thread function
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break

        print(data)
        if data[0] == "0":
            ard.action(0, box)
        elif data[0] == "1":
            ard.action(1, box)
        elif data[0] == "2":
            ard.action(2, box)
        elif data[0] == "3":
            ard.action(3, box)

        # send back reversed string to client
        c.send(data)

        # connection closed
    c.close()


def Main():
    host = "0.0.0.0"

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 6161
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()

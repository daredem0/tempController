#!/usr/bin/env python
import socket

def conTcp(TCP_IP, TCP_PORT):
    BUFFER_SIZE = 1024
    ip = [0,0,0,0]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    try:
        data = s.recv(BUFFER_SIZE)
        ssid = str(data.decode('ascii'))
        data = s.recv(BUFFER_SIZE)
        ip[0] = int(data)
        data = s.recv(BUFFER_SIZE)
        ip[1] = int(data)
        data = s.recv(BUFFER_SIZE)
        ip[2] = int(data)
        data = s.recv(BUFFER_SIZE)
        ip[3] = int(data)
        data = s.recv(BUFFER_SIZE)
        port = int(data)
        print("SSID:", ssid)
        print("IP: ", ip[0], ".", ip[1], ".", ip[2], ".", ip[3])
        print("Port: ", port)
    except:
        print("Couldnt establish Connection")
    return s


def setTemp(t, s):
    BUFFER_SIZE = 1024
    try:
        MESSAGE = str(t).encode()
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        rec = float(data.decode('ascii'))
        return rec
    except Exception as e:
        print("Couldn't send message. Error: ", str(e))
        return -1


def disTcp(s):
    try:
        s.close()
        print("Disconnected")
    except:
        print("Couldn't disconnect")

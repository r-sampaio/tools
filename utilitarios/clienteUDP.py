#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

target = "127.0.0.1"
port   = 80

openSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

openSocket.sendto(("^c").encode(),(target, port))

data, addr = openSocket.recvfrom(4096)

print(data)
openSocket.close()

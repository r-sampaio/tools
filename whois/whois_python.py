#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys

openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
openSocket.connect(("whois.iana.org",43))
openSocket.sendall((f"{sys.argv[1]}\r\n").encode())
resposta = openSocket.recv(1024)
print((resposta.decode()).split())

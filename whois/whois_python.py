#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 05/02/2021
# Author: r-sampaio
# Github: https://github.com/r-sampaio
# Python version: 3.x

import socket
import sys

def uso():
    """ Modo de Uso da ferramenta """
    print(" Modo de uso da ferramenta...")
    print(f" $ python {sys.argv[0]} target")
    sys.exit(0)


if not len(sys.argv[1:]):
    uso()

openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
openSocket.connect(("whois.iana.org",43))
openSocket.sendall((f"{sys.argv[1]}\r\n").encode())
resposta = openSocket.recv(1024)
resp = ((resposta.decode()).split())[19]
openSocket.close()

openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
openSocket.connect((resp,43))
openSocket.sendall((f"{sys.argv[1]}\r\n").encode())
resposta = openSocket.recv(1024)
print(resposta.decode(errors='ignore'))
openSocket.close()

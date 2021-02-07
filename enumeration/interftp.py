#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 06/02/2021
# Author: r-sampaio
# Github: https://github.com/r-sampaio
# Python version: 3.x

import socket
import sys


def uso():
    """ Modo de Uso da ferramenta """
    print(" Interacting with ftp server")
    print(f" $ python3 {sys.argv[0]} [target] [port] [username] [password]")
    sys.exit(0)


if not len(sys.argv[4:]):
    uso()

target   = str(sys.argv[1])
port     = int(sys.argv[2])
username = str(sys.argv[3])
password = str(sys.argv[4])

openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
openSocket.connect((target, port))
banner = openSocket.recv(1024)
print(banner.decode())

print(f"USER {username}")
openSocket.send((f"USER {username}\r\n").encode())
resposta = openSocket.recv(1024)
print(resposta.decode())

print(f"PASS {password}")
openSocket.send((f"PASS {password}\r\n").encode())
resposta = openSocket.recv(1024)
print(resposta.decode())

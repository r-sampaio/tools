#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 06/02/2021
# Author: r-sampaio
# Github: https://github.com/r-sampaio
# Python version: 3.x

import socket
import sys


def uso():
    """ Modo de uso da ferramenta """
    print(" Modo de uso da ferramenta...")
    print()
    print(" Banner Grabbing:")
    print(f" $ python3 {sys.argv[0]} host port")
    sys.exit(0)


if not len(sys.argv[1:]):
    uso()

host = str(sys.argv[1])
port = int(sys.argv[2])

openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# openSocket.connect((str(sys.argv[1]),int(sys.argv[2])))
openSocket.connect((host,port))
banner = openSocket.recv(1024)
print(banner.decode("utf-8"))

#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 06/02/2021
# Author: r-sampaio
# Github: https://github.com/r-sampaio
# Python version: 3.x

import socket
import sys


def usage():
    """ Modo de Uso da ferramenta """
    print(" Scanner all ports")
    print(f" $ python3 {sys.argv[0]} [target] [-A] (verbose - open/closed)")
    print(f" $ python3 {sys.argv[0]} [target] [-O] (verbose - open only)")
    print()
    print(" Specific port scanner")
    print(f" $ python3 {sys.argv[0]} [target] [-P] [port]")
    sys.exit(0)


if not len(sys.argv[2:]):
    usage()

print(f" Host: \033[34m{sys.argv[1]}\033[m")

if sys.argv[2] == '-P':
    if not len(sys.argv[3:]):
        usage()
    else:
        host = str(sys.argv[1])
        port = int(sys.argv[3])
        openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        poc = openSocket.connect_ex((host, port)) 
        if poc == 0:
            print(f" \033[32m[OPEN]\033[m : {sys.argv[3]}")
            openSocket.close()
        else:
            print(f" \033[31m[CLOSED]\033[m : {port}")

if sys.argv[2] == '-O':
    for port in range(1,65536):
        openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        poc = openSocket.connect_ex((sys.argv[1],port)) 
        if poc == 0:
            print(f" \033[32m[OPEN]\033[m : {port}")
            openSocket.close()

if sys.argv[2] == '-A':
    for port in range(1,65536):
        openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        poc = openSocket.connect_ex((sys.argv[1],port)) 
        if poc == 0:
            print(f" \033[32m[OPEN]\033[m : {port}")
            openSocket.close()
        else:
            print(f" \033[31m[CLOSED]\033[m : {port}")

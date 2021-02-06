#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 06/02/2021
# Author: r-sampaio
# Github: https://github.com/r-sampaio
# Python version: 3.x

import socket
import sys


def conecta(target, port, conteudo):
    openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    openSocket.connect((target, port))
    openSocket.send(conteudo.encode())
    return openSocket


def usage():
    """ Modo de Uso da ferramenta """
    print(" Cliente TCP porta 80:")
    print(f" $ python3 {sys.argv[0]} [http_version] [method] [page] [target]")
    print("   http_version = -A - HTTP/1.0")
    print("                  -B - HTTP/1.1")
    print("   method       = GET, HEAD, PUT, POST...")
    print("   page         = /, /page")
    print("   target       = Host address")
    sys.exit(0)


if not len(sys.argv[4:]):
    usage()

target = f"{sys.argv[4]}"
port = 80
if sys.argv[1] == '-A':
    conteudo = f"{sys.argv[2]} {sys.argv[3]} HTTP/1.0\r\n\r\n"
if sys.argv[1] == '-B':
    conteudo = f"{sys.argv[2]} {sys.argv[3]} HTTP/1.1\r\nHost: {sys.argv[4]}\r\n\r\n"

openSocket = conecta(target, port, conteudo)
resposta = openSocket.recv(4096)
print(resposta.decode())
openSocket.close()

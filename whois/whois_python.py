#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
import os

def limpa():
    """ Limpa a tela do terminal """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


limpa()

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
print(resposta.decode(encoding='utf-8', errors='ignore'))
openSocket.close()

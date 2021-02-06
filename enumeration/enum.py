#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 06/02/2021
# Author: r-sampaio
# Github: https://github.com/r-sampaio
# Python version: 3.x

import socket
import sys
import os


def limpa():
    """ Limpa a tela do terminal """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def uso():
    """ Modo de Uso da ferramenta """
    print(" Modo de uso da ferramenta...")
    print()
    print(" Port scanner:")
    print(f" $ python3 {sys.argv[0]} target")
    sys.exit(0)


limpa()

if not len(sys.argv[1:]):
    uso()

print(f"Host: \033[34m{sys.argv[1]}\033[m")
for port in range(1,65536):
    openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    poc = openSocket.connect_ex((sys.argv[1],port)) 
    if poc == 0:
        print(f" \033[32m[OPEN]\033[m : {port}")
        openSocket.close()

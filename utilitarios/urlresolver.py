#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 07/02/2021
# Author: r-sampaio
# Github: https://github.com/r-sampaio
# Python version: 3.x

import socket
import sys
import urllib3


def usage():
    """ Usage mode """
    print(f" DNS resolver           $ python3 {sys.argv[0]} [-r] [target]")
    print(f" Brute force subdomain  $ python3 {sys.argv[0]} [-s] [target] [wordlist]")
    print(f" Brute force directory  $ python3 {sys.argv[0]} [-d] [target] [wordlist]")
    print(f" Brute force archive    $ python3 {sys.argv[0]} [-a] [target] [wordlist] [EXT]")
    sys.exit(0)


if not len(sys.argv[1:]):
    usage()

option = sys.argv[1]

if option == '-r':
    if not len(sys.argv[2:]):
        usage()
    target = sys.argv[2]
    host = socket.gethostbyname(target)
    print(f"[\033[32m{host:^15}\033[m]  {target}")

if option == '-s':
    if not len(sys.argv[3:]):
        usage()
    target = sys.argv[2]
    lista  = sys.argv[3]
    host = socket.gethostbyname(target)
    print(f"[\033[32m{host:^15}\033[m]  {target}")
    with open(lista,'r') as wordlist:
        for dns in wordlist:
            try:
                hostname = f"{dns.strip()}.{target.strip()}"
                host = socket.gethostbyname(hostname)
                print(f"[\033[32m{host:^15}\033[m]  {hostname}")
            except:
                print(end='')

if option == '-d':
    if not len(sys.argv[3:]):
        usage()
    target = sys.argv[2]
    lista  = sys.argv[3]
    with open(lista,'r') as wordlist:
        for directory in wordlist:
            try:
                hostname = f"{target.strip()}/{directory.strip()}/"
                host = urllib3.PoolManager()
                response = host.request('GET', hostname)
                code_status = response.status
                if code_status >= 200 and code_status < 300:
                    print(f"\033[32m[{code_status}]\033[m  {hostname}")
                elif code_status >= 300 and code_status < 400:
                    print(f"\033[33m[{code_status}]\033[m  {hostname}")
            except:
                print(end='')

if option == '-a':
    if not len(sys.argv[4:]):
        usage()
    target = sys.argv[2]
    lista  = sys.argv[3]
    ext    = sys.argv[4]
    with open(lista,'r') as wordlist:
        for arquivo in wordlist:
            try:
                hostname = f"{target.strip()}/{arquivo.strip()}.{ext.strip()}"
                host = urllib3.PoolManager()
                response = host.request('GET', hostname)
                code_status = response.status
                
                if code_status >= 200 and code_status < 300:
                    print(f"\033[32m[{code_status}]\033[m  {hostname}")
                elif code_status >= 300 and code_status < 400:
                    print(f"\033[33m[{code_status}]\033[m  {hostname}")
            except:
                print(end='')

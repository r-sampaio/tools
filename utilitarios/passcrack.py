#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 13/02/2021
# Author: r-sampaio
# Github: https://github.com/r-sampaio
# Python version: 3.x

import hashlib
import base64
import sys
import os

def usage():
    """ Modo de Uso da ferramenta """
    print(f" $ python3 {sys.argv[0]} [-b] [encode/decode] [data]")
    print()
    print(f" $ python3 {sys.argv[0]} [-c] [hash-less-salt] [wordlist]")
    print(f"   Salt: $6$AUJwtii8yHc4Tws7$")
    print("   # Linux only")
    print()
    print(f" $ python3 {sys.argv[0]} [-s] [hash] [data] [wordlist]")
    print("   # Hashs suportados:")
    print("   - sha-1, sha-224, sha-256, sha-384, sha-512")
    print("   - sha-3-224, sha-3-256, sha-3-384, sha-3-512")
    print("   - blake-2B, blake-2S")
    print("   - shake-128, shake-256")
    print("   - md5")
    sys.exit(0)


if not len(sys.argv[3:]):
    usage()

argumento  = sys.argv[1]
opcao_hash = sys.argv[2]
texto_user = sys.argv[3]

if argumento == '-b':
    text = texto_user.encode()
    if opcao_hash == 'encode':
        r = base64.b64encode(text)
    if opcao_hash == 'decode':
        r = base64.b64decode(text)
    print((r.decode()).strip())

if argumento == '-s':
    if not len(sys.argv[4:]):
        usage()
    lista = sys.argv[4]
    with open(lista, 'r') as arquivo:
        for palavra in arquivo:
            sEnter = palavra.strip()
            texto = sEnter.encode()
            if opcao_hash == 'sha-1':
                hash = hashlib.sha1(texto)
            if opcao_hash == 'sha-224':
                hash = hashlib.sha224(texto)
            if opcao_hash == 'sha-256':
                hash = hashlib.sha256(texto)
            if opcao_hash == 'sha-384':
                hash = hashlib.sha384(texto)
            if opcao_hash == 'sha-512':
                hash = hashlib.sha512(texto)
            if opcao_hash == 'sha-3-224':
                hash = hashlib.sha3_224(texto)
            if opcao_hash == 'sha-3-256':
                hash = hashlib.sha3_256(texto)
            if opcao_hash == 'sha-3-384':
                hash = hashlib.sha3_384(texto)
            if opcao_hash == 'sha-3-512':
                hash = hashlib.sha3_512(texto)
            if opcao_hash == 'blake-2b':
                hash = hashlib.blake2b(texto)
            if opcao_hash == 'blake-2S':
                hash = hashlib.blake2s(texto)
            if opcao_hash == 'md5':
                hash = hashlib.md5(texto)
            if opcao_hash == 'shake-128':
                hash = hashlib.shake_128(texto)
            if opcao_hash == 'shake-256':
                hash = hashlib.shake_256(texto)

            text = hash.hexdigest()
            if text == texto_user:
                print(f"{palavra.strip()} : {text}")
                sys.exit(0)


if os.name != 'nt':
    import crypt

    if argumento == '-c':
        salt_hash = str(input('Salt: '))
        senha_user = salt_hash + opcao_hash
        lista = sys.argv[3]
        with open(lista, 'r') as arquivo:
            for palavra in arquivo:
                senha = palavra.strip()
                resposta = crypt.crypt(senha, salt_hash)
                if resposta == senha_user:
                    print(f"{palavra.strip()} : {senha_user}")
                    sys.exit(0)

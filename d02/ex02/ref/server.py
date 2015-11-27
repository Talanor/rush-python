#!/usr/bin/env python3

import socket
import sys
import multiprocessing
import hashlib
import wash

def handler(sock, addr):
    data = sock.recv(9)
    if data.decode('utf-8').endswith('\n'):
        data = data.decode('utf-8')[:-1]
    retData = wash.stringWash(bytes(data, 'ascii'))
    sock.send(bytes(retData, 'ascii'))
    hash_data = sock.recv(1024).decode('utf-8').split()[0]
    if hash_data == hashlib.sha512(bytes(retData, 'ascii')).hexdigest():
        sock.send(b'GG IT WORKS')
    else:
        sock.send(b'such a bad token ...')
    return 0

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((sys.argv[1], int(sys.argv[2])))
    except Exception as e:
        print (e)
        print('usage: python server.py <ip> <port>')
        sys.exit(1)
    sock.listen(5)
    while True:
        (c_sock, addr) = sock.accept()
        p = multiprocessing.Process(target=handler, args=(c_sock, addr))
        p.start()

#!/usr/bin/env python3

import socket
import sys
import multiprocessing
import hashlib
import wash

def handler(sock, addr):
    data = sock.recv(9)
    try:
        if data.decode('utf-8').endswith('\n'):
            data = data.decode('utf-8')[:-1]
        print(data + ' is trying hard...')
        retData = wash.stringWash(bytes(data, 'ascii'))
        sock.send(bytes(retData, 'ascii'))
        hash_data = sock.recv(128).decode('utf-8').split()[0]
        if hash_data == hashlib.sha512(bytes(retData, 'ascii')).hexdigest():
            sock.send(b'\nGG IT WORKS\n')
            print(data + ' done it!')
        else:
            sock.send(b'\nsuch a bad token...\n')
            print(data + ' failed it!')
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return 0
    except:
        print(addr, 'failed hardly!')

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


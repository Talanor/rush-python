#!/usr/bin/env python3
from hashlib import sha512
words = [sha512(bytes(word[::-1], 'ascii')).hexdigest() for word in open('data.txt', 'r').read().split(' ') if len(word) > 2]
print('l33t\n'.join([words[i][:i+1] for i in range(len(words))]), end='l33t\n')

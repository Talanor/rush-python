#!/usr/bin/python3
## bistromatique.py for  in /home/sin/cq-proj/rush-python/d01/ex03/ref
##
## Made by SiN
## Login   <sin@epitech.net>
##
## Started on  Fri Oct 30 20:04:26 2015 
## Last update Fri Oct 30 20:08:53 2015 
##

import sys

allow = '0123456789+*-/%'

try:
    for i in sys.argv[1]:
        if i not in allow:
            sys.exit(0)
    print(eval(sys.argv[1]))
except Exception as e:
    print(e)

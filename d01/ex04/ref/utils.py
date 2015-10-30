#!/usr/bin/python2.7
## utils.py for  in /home/sin/cq-proj/rush-python/d01/ex04/ref
##
## Made by SiN
## Login   <sin@epitech.net>
##
## Started on  Fri Oct 30 20:09:49 2015 
## Last update Fri Oct 30 20:23:56 2015 
##

def dislok(string):
    return string.split(' ')

def sort_list(lst):
    return lst.sort()

def rev_it(par):
    if isinstance(par, str):
        ret = ''.join([_ for _ in reversed(par)])
    elif isinstance(par, list):
        ret = [_ for _ in reversed(par)]
    else:
        return None
    return ret

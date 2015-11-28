#!/usr/bin/python2.7
## pyls.py for  in /home/sin/CQ/rush-python/d02/ex04/ref
##
## Made by SiN
## Login   <sin@epitech.net>
##
## Started on  Sat Nov 28 14:19:20 2015 
## Last update Sat Nov 28 14:43:42 2015 
##

import sys
import os
import stat
import pwd
import grp
import time

def prettify(path):
    data = os.stat(path)
    return '%s %d %s %s %d %s %s' % (
        stat.filemode(data.st_mode),
        data.st_nlink,
        pwd.getpwuid(data.st_uid).pw_name,
        grp.getgrgid(data.st_gid).gr_name,
        data.st_size,
        time.ctime(data.st_mtime),
        path.split('/')[-1]
    )

def printFl(name: str, pretty: bool) -> None:
    printed = []
    for fl in os.listdir(name):
        if pretty:
            printed.append(prettify('/'.join([name, fl])))
        else:
            printed.append(fl)
    print('\n'.join(printed))

if __name__ == '__main__':
    isL = False
    if '-l' in sys.argv:
        isL = True
    for folder in sys.argv[1:]:
        if folder.startswith('-'):
            continue
        printFl(folder, isL)
    else:
        printFl('./', isL)

#!/usr/bin/python2.7
## myfirstclass.py for  in /home/sin/CQ/rush-python/d01/ex09/ref
##
## Made by SiN
## Login   <sin@epitech.net>
##
## Started on  Fri Nov 27 22:51:13 2015 
## Last update Sat Nov 28 10:52:47 2015 
##

class FirstClass(object):

    def __init__(string):
        super(FirstClass, self).__init__()
        self.string = string

    @staticmethod
    def persFunc():
        pass

    def hashIt(self, hashes=self.persFunc):
        try:
            return hashes(self.string)
        except:
            return 'you lame'

    @staticmethod
    def hashParam(string, hashes=self.persFunc):
        try:
            return hashes(self.string)
        except:
            return 'you lame'

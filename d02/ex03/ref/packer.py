#!/usr/bin/python3

import struct

class packer(object):

    def __init__():
        super(packer, self).__init__()

    @staticmethod
    def networkPackData(*args, **kwargs):
        _format = '!'
        for item in args:
            if type(item) is int:
                format += 'I'
            elif type(item) is str:
                format += '%ds' % (len(item))
            elif type(item) is float:
                format += 'f'
        return struct.pack(_format, *args)

    @staticmethod
    def bigEndianPackData(*args, **kwargs):
        _format = '>'
        for item in args:
            if type(item) is int:
                format += 'I'
            elif type(item) is str:
                format += '%ds' % (len(item))
            elif type(item) is float:
                format += 'f'
        return struct.pack(_format, *args)


    @staticmethod
    def littleEndian(*args, **kwargs):
        _format = '<'
        for item in args:
            if type(item) is int:
                format += 'I'
            elif type(item) is str:
                format += '%ds' % (len(item))
            elif type(item) is float:
                format += 'f'
        return struct.pack(_format, *args)

    @staticmethod
    def unpackAllDatas(form, data):
        return struct.unpack(form, data)

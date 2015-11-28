#!/usr/bin/python3

import struct

class packer(object):

    def __init__():
        super(packer, self).__init__()

    @staticmethod
    def networkPackData(*args, **kwargs):
        _format = '!'
        data = []
        for item in args:
            if type(item) is int:
                _format += 'I'
                data.append(item)
            elif type(item) is str:
                _format += '%ds' % (len(item))
                data.append(bytes(item, 'ascii'))
            elif type(item) is float:
                _format += 'f'
                data.append(bytes(item, 'ascii'))
            else:
                raise NotImplementedError
        return struct.pack(_format, *data)

    @staticmethod
    def bigEndianPackData(*args, **kwargs):
        _format = '>'
        data = []
        for item in args:
            if type(item) is int:
                _format += 'I'
                data.append(item)
            elif type(item) is str:
                _format += '%ds' % (len(item))
                data.append(bytes(item, 'ascii'))
            elif type(item) is float:
                _format += 'f'
                data.append(bytes(item, 'ascii'))
            else:
                raise NotImplementedError
        return struct.pack(_format, *data)


    @staticmethod
    def littleEndian(*args, **kwargs):
        _format = '<'
        data = []
        for item in args:
            if type(item) is int:
                _format += 'I'
                data.append(item)
            elif type(item) is str:
                _format += '%ds' % (len(item))
                data.append(bytes(item, 'ascii'))
            elif type(item) is float:
                _format += 'f'
                data.append(bytes(item, 'ascii'))
            else:
                raise NotImplementedError
        return struct.pack(_format, *data)

    @staticmethod
    def unpackAllDatas(form, data):
        return struct.unpack(form, data)

if __name__ == '__main__':
    print (packer.networkPackData(8,9,'koala'))

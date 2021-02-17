"""
Module: 'ustruct' on micropython-esp32-1.14
"""
# MCU: {'ver': '1.14', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.14.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.14.0', 'machine': 'ESP32 module with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.9
import struct as _struct

def calcsize(fmt) -> int:
    '''Return the number of bytes needed to store the given fmt.'''
    return _struct.calcsize(fmt)

def pack(fmt, *v) -> bytes:
    '''Pack the values v1, v2, … according to the format string fmt.
    Return value is a bytes object encoding the values.'''
    return _struct.pack(fmt, *v)

def pack_into(fmt, buffer, offset, *v) -> None:
    '''
    Pack the values v1, v2, … according to the format string fmt into a buffer starting at offset.
    offset may be negative to count from the end of buffer.
    '''
    _struct.pack_into(fmt, buffer, offset, *v)

def unpack(fmt, buf) -> tuple:
    '''
    Unpack from the data according to the format string fmt.
    Return value is a tuple of the unpacked values.
    '''
    return _struct.unpack(fmt, buf)

def unpack_from(fmt, buffer, offset=0) -> tuple:
    '''
    Unpack from the data starting at offset according to the format string fmt.
    offset may be negative to count from the end of buffer.
    Return value is a tuple of the unpacked values.
    '''
    _struct.unpack_from(fmt, buffer, offset=0)

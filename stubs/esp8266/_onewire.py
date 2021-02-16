# frozen onewire module imports a _onewire module

from random import randint

def crc8(data):
    # onewire module implies this returns something. assuming it's boolean
    return True

def readbit(pin):
    return randint(0, 1)

def readbyte(pin):
    return randint(0, 2**8-1)

def reset(pin):
    return True

def writebit(pin, value):
    # onewire module implies this returns something. assuming it's boolean
    return True

def writebytepin(pin, value):
    # onewire module implies this returns something. assuming it's boolean
    return True

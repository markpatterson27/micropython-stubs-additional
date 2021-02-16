# frozen onewire module imports a _onewire module

from random import randint

bit = 0

def crc8(data):
    # onewire module implies this returns something. assuming it's boolean
    return True

def readbit(pin):
    # seems if this gives two 1's in row, implies no device
    global bit
    if bit == 1:
        bit = 0
    else:
        bit = randint(0, 1)
    return bit

def readbyte(pin):
    return randint(0, 2**8-1)

def reset(pin):
    return True

def writebit(pin, value):
    # onewire module implies this returns something. assuming it's boolean
    return True

def writebyte(pin, value):
    # onewire module implies this returns something. assuming it's boolean
    return True

"""
Module: 'machine' on micropython-esp32-1.14
"""
# MCU: {'ver': '1.14', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.14.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.14.0', 'machine': 'ESP32 module with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.9

from random import randint

class ADC:
    ''
    ATTN_0DB = 0
    ATTN_11DB = 3
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    WIDTH_10BIT = 1
    WIDTH_11BIT = 2
    WIDTH_12BIT = 3
    WIDTH_9BIT = 0
    def atten():
        pass

    def read():
        pass

    def read_u16():
        pass

    def width():
        pass


class DAC:
    ''
    def write():
        pass

DEEPSLEEP = 4
DEEPSLEEP_RESET = 4
EXT0_WAKE = 2
EXT1_WAKE = 3
HARD_RESET = 2

class I2C:
    '''There are two hardware I2C peripherals with identifiers 0 and 1. Any available output-capable pins can be used for SCL and SDA'''
    
    def init(id, *, scl, sda, freq=400000):
        '''
        Construct a new software I2C object.

        param

        id - identifies a particular I2C peripheral. Allowed values are 0 or 1.
        scl - pin object specifying the pin to use for SCL.
        sda - pin object specifying the pin to use for SDA.
        freq - integer which sets the maximum frequency for SCL.
        '''
        pass

    def readfrom(self, addr, nbytes, stop=True):
        '''
        Read nbytes from the slave specified by addr. If stop is true then a STOP condition is generated at the end of the transfer.
        
        Returns a bytes object with the data read.
        '''
        return [randint(0, 2**8-1)]*nbytes

    def readfrom_into(self, addr, buf, stop=True):
        '''
        Read into buf from the slave specified by addr. The number of bytes read will be the length of buf. If stop is true then a STOP condition is generated at the end of the transfer.

        Returns None.
        '''
        return None

    def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize=8):
        '''
        Read nbytes from the slave specified by addr starting from the memory address specified by memaddr. The argument addrsize specifies the address size in bits.
        
        Returns a bytes object with the data read.
        '''
        return [randint(0, 2**8-1)]*nbytes

    def readfrom_mem_into(self, addr, memaddr, buf, *, addrsize=8):
        '''
        Read into buf from the slave specified by addr starting from the memory address specified by memaddr. The number of bytes read is the length of buf. The argument addrsize specifies the address size in bits (on ESP8266 this argument is not recognised and the address size is always 8 bits).

        Returns None.
        '''
        return None

    def readinto(self, buf, nack=True):
        '''
        Reads bytes from the bus and stores them into buf. The number of bytes read is the length of buf. An ACK will be sent on the bus after receiving all but the last byte. After the last byte is received, if nack is true then a NACK will be sent, otherwise an ACK will be sent (and in this case the slave assumes more bytes are going to be read in a later call).
        '''
        pass

    def scan(self):
        '''Scan all I2C addresses between 0x08 and 0x77 inclusive. Returns a list of those that respond.'''
        pass

    def start(self):
        '''Generate a START condition on the bus (SDA transitions to low while SCL is high).'''
        pass

    def stop(self):
        '''Generate a STOP condition on the bus (SDA transitions to high while SCL is high).'''
        pass

    def write(self, buf):
        '''
        Write the bytes from buf to the bus. Checks that an ACK is received after each byte and stops transmitting the remaining bytes if a NACK is received.
        
        Returns the number of ACKs that were received.
        '''
        return len(buf)

    def writeto(self, addr, buf, stop=True):
        '''
        Write the bytes from buf to the slave specified by addr. If a NACK is received following the write of a byte from buf then the remaining bytes are not sent. If stop is true then a STOP condition is generated at the end of the transfer, even if a NACK is received.
        
        Returns the number of ACKs that were received.
        '''
        return len(buf)

    def writeto_mem(self, addr, memaddr, buf, *, addrsize=8):
        '''
        Write buf to the slave specified by addr starting from the memory address specified by memaddr. The argument addrsize specifies the address size in bits (on ESP8266 this argument is not recognised and the address size is always 8 bits).

        Returns None.
        '''
        return None

    def writevto(self, addr, vector, stop=True):
        '''
        Write the bytes contained in vector to the slave specified by addr. vector should be a tuple or list of objects with the buffer protocol. The addr is sent once and then the bytes from each object in vector are written out sequentially. The objects in vector may be zero bytes in length in which case they don’t contribute to the output.

        If a NACK is received following the write of a byte from one of the objects in vector then the remaining bytes, and any remaining objects, are not sent. If stop is true then a STOP condition is generated at the end of the transfer, even if a NACK is received.
        
        Returns the number of ACKs that were received.
        '''
        return len(vector)

PIN_WAKE = 2

class PWM:
    ''
    def deinit():
        pass

    def duty():
        pass

    def freq():
        pass

    def init():
        pass

PWRON_RESET = 1

class Pin:
    '''Access the pin peripheral (GPIO pin) associated with the given id.'''
    IN = 1
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 3
    PULL_DOWN = 1
    PULL_HOLD = 4
    PULL_UP = 2
    WAKE_HIGH = 5
    WAKE_LOW = 4
    
    def init(self, pin_id, mode=- 1, pull=- 1, *, value=0, drive, alt):
        self._value = value

    def irq(self, handler=None, trigger=IRQ_FALLING|IRQ_RISING, *, priority=1, wake=None, hard=False):
        '''
        Configure an interrupt handler to be called when the trigger source of the pin is active.
        
        Params

        handler: optional function to be called when the interrupt triggers. The handler must take exactly one argument which is the Pin instance.
        trigger: configures the event which can generate an interrupt. Possible values are:
          - Pin.IRQ_FALLING interrupt on falling edge.
          - Pin.IRQ_RISING interrupt on rising edge.

        Returns callback object
        '''
        pass

    def off(self):
        '''Set pin to “0” output level.'''
        self._value = 0

    def on(self):
        '''Set pin to “1” output level.'''
        self._value = 1

    def value(self, val=None):
        '''Set and get the value of the pin, depending on whether the argument val is supplied or not.'''
        if val is None:
            return self._value
        else:
            self._value = val
            return None


class RTC:
    ''
    def datetime():
        pass

    def init():
        pass

    def memory():
        pass


class SDCard:
    ''
    def deinit():
        pass

    def info():
        pass

    def ioctl():
        pass

    def readblocks():
        pass

    def writeblocks():
        pass

SLEEP = 2
SOFT_RESET = 5

class SPI:
    ''
    LSB = 1
    MSB = 0
    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


class Signal:
    ''
    def off():
        pass

    def on():
        pass

    def value():
        pass


class SoftI2C(I2C):
    '''Software I2C (using bit-banging) works on all output-capable pins'''

    def init(self, scl, sda, *, freq=400000, timeout=255):
        '''
        Construct a new software I2C object.

        param

        scl - pin object specifying the pin to use for SCL.
        sda - pin object specifying the pin to use for SDA.
        freq - integer which sets the maximum frequency for SCL.
        timeout - the maximum time in microseconds to wait for clock stretching (SCL held low by another device on the bus), after which an OSError(ETIMEDOUT) exception is raised.
        '''
        pass

    ## methods should be inherited from I2C

    # def readfrom():
    #     pass

    # def readfrom_into():
    #     pass

    # def readfrom_mem():
    #     pass

    # def readfrom_mem_into():
    #     pass

    # def readinto():
    #     pass

    # def scan():
    #     pass

    # def start():
    #     pass

    # def stop():
    #     pass

    # def write():
    #     pass

    # def writeto():
    #     pass

    # def writeto_mem():
    #     pass

    # def writevto():
    #     pass


class SoftSPI:
    ''
    LSB = 1
    MSB = 0
    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass

TIMER_WAKE = 4
TOUCHPAD_WAKE = 5

class Timer:
    ''
    ONE_SHOT = 0
    PERIODIC = 1
    def deinit():
        pass

    def init():
        pass

    def value():
        pass


class TouchPad:
    ''
    def config():
        pass

    def read():
        pass


class UART:
    ''
    INV_CTS = 1048576
    INV_RTS = 8388608
    INV_RX = 524288
    INV_TX = 4194304
    def any():
        pass

    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def readline():
        pass

    def sendbreak():
        pass

    def write():
        pass

ULP_WAKE = 6

class WDT:
    ''
    def feed():
        pass

WDT_RESET = 3
def deepsleep():
    pass

def disable_irq():
    pass

def enable_irq():
    pass

def freq():
    pass

def idle():
    pass

def lightsleep():
    pass

mem16 = None
mem32 = None
mem8 = None
def reset():
    pass

def reset_cause():
    pass

def sleep():
    pass

def soft_reset():
    pass

def time_pulse_us():
    pass

def unique_id():
    pass

def wake_reason():
    pass


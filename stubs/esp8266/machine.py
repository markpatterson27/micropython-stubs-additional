"""
Module: 'machine' on micropython-esp8266-2.0.0(5a875ba)
"""
# MCU: {'ver': '2.0.0(5a875ba)', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '2.0.0(5a875ba)', 'name': 'micropython', 'mpy': 9733, 'version': '1.14.0', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.3.9

from random import randint

class ADC:
    ''
    def read():
        pass

    def read_u16():
        pass

DEEPSLEEP = 4
DEEPSLEEP_RESET = 5
HARD_RESET = 6

class SoftI2C:
    '''The I2C driver is implemented in software and works on all pins'''

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


I2C = SoftI2C


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

PWRON_RESET = 0

class Pin:
    '''Access the pin peripheral (GPIO pin) associated with the given id.'''
    IN = 0
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 2
    OUT = 1
    PULL_UP = 1
    
    def __init__(self, pin_id, mode=- 1, pull=- 1, **kwargs):
        '''
        params:
        mode
        pull
        value
        drive
        alt
        '''
        self._value = kwargs.get('value', 0)

    def init(self, mode=- 1, pull=- 1, **kwargs):
        '''
        Re-initialise the pin using the given parameters.

        params:
        mode
        pull
        value
        drive
        alt

        Returns None.
        '''
        self._value = kwargs.get('value', 0)
        return None

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
    ALARM0 = 0
    def alarm():
        pass

    def alarm_left():
        pass

    def datetime():
        pass

    def irq():
        pass

    def memory():
        pass

SOFT_RESET = 4

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


class Timer:
    ''
    ONE_SHOT = 0
    PERIODIC = 1
    def deinit():
        pass

    def init():
        pass


class UART:
    ''
    def any():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def readline():
        pass

    def write():
        pass


class WDT:
    ''
    def deinit():
        pass

    def feed():
        pass

WDT_RESET = 1
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


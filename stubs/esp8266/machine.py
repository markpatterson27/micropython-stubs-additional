"""
Module: 'machine' on micropython-esp8266-2.0.0(5a875ba)
"""
# MCU: {'ver': '2.0.0(5a875ba)', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '2.0.0(5a875ba)', 'name': 'micropython', 'mpy': 9733, 'version': '1.14.0', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.3.9

class ADC:
    ''
    def read():
        pass

    def read_u16():
        pass

DEEPSLEEP = 4
DEEPSLEEP_RESET = 5
HARD_RESET = 6

class I2C:
    ''
    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def readinto():
        pass

    def scan():
        pass

    def start():
        pass

    def stop():
        pass

    def write():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

    def writevto():
        pass


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


class SoftI2C:
    ''
    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def readinto():
        pass

    def scan():
        pass

    def start():
        pass

    def stop():
        pass

    def write():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

    def writevto():
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


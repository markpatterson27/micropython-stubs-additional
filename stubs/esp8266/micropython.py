"""
Module: 'micropython' on micropython-esp32-1.14
"""
# MCU: {'ver': '1.14', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.14.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.14.0', 'machine': 'ESP32 module with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.9
def alloc_emergency_exception_buf():
    pass

def const(expr) -> int:
    '''Used to declare that the expression is a constant so that the compile can optimise it.'''
    return int(expr)

def heap_lock():
    pass

def heap_unlock():
    pass

def kbd_intr():
    pass

def mem_info():
    pass

def opt_level():
    pass

def qstr_info():
    pass

def schedule():
    pass

def stack_use():
    pass

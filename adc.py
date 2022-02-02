#import os as _os
from mmap import mmap as _mm
from importlib import import_module as _il
from ctypes import c_uint32 as _ct


class Setup():
  def __init__(self, board):
    global device, region
    device = _il("AMPatio.models."+board['SOC']+".ADC")
    device.headers = board['GPIO']
    #
    #size = os.sysconf(os.sysconf_names["SC_PAGESIZE"])
    size = (1024*4) # 1024*4
    #
    #file = os.open("/dev/mem", os.O_RDWR | os.O_SYNC)
    with open("/dev/mem", "rb+") as file:
       region = _mm(file.fileno(), size, offset=device.address)
### End of class Setup ########################################################


class Channel():
  def __init__(self, pin: int):
    """ pin: Pin number from the board header.
    """
    self.pin = pin

    # get pin register, bit location
    self.register, self.channel = tuple(device.headers[pin].items())[0]

#  ISC
#
#  Copyright (c) 2022 Adir Vered <adir.vrd@gmail.com>
#
#  Permission to use, copy, modify, and/or distribute this software for any purpose
#  with or without fee is hereby granted, provided that the above copyright notice
#  and this permission notice appear in all copies.
#
#  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
#  REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
#  AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
#  INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
#  LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
#  OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE
#  OR PERFORMANCE OF THIS SOFTWARE.
#

#import os as _os
from mmap import mmap as _mm
from importlib import import_module as _il
#from pkgutil import get_data as _pugd
#from ast import literal_eval as _astle
from ctypes import c_uint32 as _cui
#from ctypes import pointer as _ptr

__name__ = "GPIO"

class Setup():
  def __init__(self, board):
    """ board: Board as variable or AMPatio direct call to boards() with board name as argument
    """
    global device, region

    device = _il("AMPatio.models."+board["SOC"]+".GPIO")
    # importlib expose the readed file as "models" to the user i don't like side effect
    # need to complete the move to pkgutil..
    #device_file = _pugd(__package__, "models/"+board["SOC"]+"/"+__name__+".py")
    #device = _astle(device_file.decode("UTF-8"))

    device.headers = board["GPIO"]
    region = [*range(2)] #list(range(2))

    #size = os.sysconf(os.sysconf_names["SC_PAGESIZE"])
    size = (1024*4) # 1024*4

    #file = os.open("/dev/mem", os.O_RDWR | os.O_SYNC)
    with open("/dev/mem", "rb+") as file:
      for i in region:
        region[i] = _mm(file.fileno(), size, offset=device.address[i])
  ### Setup EoC


class Pin():
  def __init__(self, pin: int, EN=0, OP=0, UP=0):
    """ pin: Pin number from the board header.
        EN(Pin function type on init): 1 MUX mode, 2 GPIO mode.
        OP(Pin output level init): 1 high level, 2 low level.
        UP(Pin pull resistor init): 1 pull up, 2 pull down & 3 off.
        * EN/OP/UP set to 0 as default, it's stand for ignore & use current pin state.
    """
    self.pin = pin

    # get pin register, bit location
    self.register, self.bit = tuple(device.headers[pin].items())[0]

    # set local region for faster respond
    _region = region[1] if self.register == "AO" else region[0]

    for i in ["O_EN", "O", "I", "UP_EN", "UP"]:
      # pre calculate pin "top" and "not" mask with 32 bits length maximum
      try:
        if (shift := device.presets[self.register][i]):
          if (i == "I"):
            self.bin = self.bit + shift
          else:
            setattr(self, "_"+i+"_top", _cui(1<<(self.bit+shift)).value)
            setattr(self, "_"+i+"_not", _cui(~(1<<(self.bit+shift))).value)
      except:
        if (i == "I"):
          self.bin = self.bit
        else:
          setattr(self, "_"+i+"_top", _cui(1<<self.bit).value)
          setattr(self, "_"+i+"_not", _cui(~(1<<self.bit)).value)
      finally:
        # set the pin control type registers & they offsets (fixd memory pointers)
        # as in the datasheets the offset is multpile by 4
        setattr(self, "_"+i, _cui.from_buffer(_region, device.offsets[self.register][i] * 4))

    # set type of the output function (MUX or GPIO)
    if (EN != 0):
      if (EN == 1):
        self._O_EN.value |= self._O_EN_top
      elif (EN == 2):
        self._O_EN.value &= self._O_EN_not

    # set default out mode (On or Off)
    if (OP != 0):
      if (OP == 1):
        self._O.value |= self._O_top
      elif (OP == 2):
        self._O.value &= self._O_not

    # set pull resistor state
    if (UP != 0):
      if (UP != 3):
        if (UP == 1):
          # set with pull up resistor
          self._UP.value |= self._UP_top
        elif (UP == 2):
          # set with pull down resistor
          self._UP.value &= self._UP_not
        self._UP_EN.value |= self._UP_EN_top
      else: #(UP == 3):
        # disable pad pull resistor
        self._UP_EN.value &= self._UP_EN_not
  ### __init__ EoF(unction)


  # just for testing dunger method...
  #def __dir__(self):
  #  return device.headers


  def alt_fun_off(self) -> None:
    """ function to set output to low level
        also set the input register as high level signal """
    self._O_EN.value &= self._O_EN_not

  def alt_fun_on(self) -> None:
    """ function to set output to high level
        also set the input register as low level signal """
    self._O_EN.value |= self._O_EN_top

  def off(self) -> None:
    """ function to set output to low level
        also set the input register as high level signal """
    self._O.value &= self._O_not

  def on(self) -> None:
    """ function to set output to high level
        also set the input register as low level signal """
    self._O.value |= self._O_top

  def toggle(self) -> None:
    """ function to toggle output or input from low to high level and from high to low level """
    self._O.value ^= self._O_top

  def level(self) -> bool:
    """ function to read pin level (by using the input register)
        this function will return 1 for high level state & 0 for low level state """
    return (self._I.value >> self.bin) & 1

  def pull_off(self) -> None:
    """ function to set internal pull resistor to off """
    self._UP_EN.value &= self._UP_EN_not

  def pull_on(self) -> None:
    """ function to set internal pull resistor to on """
    self._UP_EN.value |= self._UP_EN_top

  def pull_down(self) -> None:
    """ function to set internal pull resistor to down """
    self._UP.value &= self._UP_not

  def pull_up(self) -> None:
    """ function to set internal pull resistor to up """
    self._UP.value |= self._UP_top
  ### Pin EoC


class LED(Pin):
  """ pre defind LED class based on Pin class
      writing this pin is done by the LED.on()/off()/toggle() methods"""
  def __init__(self, pin: int):
    super().__init__(pin, 2, 2, 3)


class BTN(Pin):
  """ pre defind Button class based on Pin class
      reading this pin is done by the BTN.level() method"""
  def __init__(self, pin: int):
    super().__init__(pin, 2, 1, 1)

#!/bin/python

import mmap
from ctypes import c_uint32

with open('/dev/mem', 'r+b') as fd:
  region = mmap.mmap(fd.fileno(), (1024), offset=0xFF809000)

#memoryview(region).hex()
#ctypes.c_uint32.from_buffer(region, 0x0 * 4).value ^= (1<<0)

# get specific bit value:
def getVal(adr=0, pin=0, pinStart=None):
  if (pinStart == None):
    return bin(c_uint32.from_buffer(region, adr * 4).value)[2:][::-1][(pin):(pin)+1][::-1]
  elif (type(pinStart) is int and pinStart < pin):
    return bin(c_uint32.from_buffer(region, adr * 4).value)[2:][::-1][(pinStart):(pin)+1][::-1]

#def letsdo(d):
#  for i in range(d):
#    print(bin(ctypes.c_uint32.from_buffer(region, i * 4).value))
#
#letsdo(16)

#!/bin/python

import mmap
from ctypes import c_uint32 as _cui

buffer = _cui.from_buffer

with open('/dev/mem', 'r+b') as fd:
  region = mmap.mmap(fd.fileno(), (1024), offset=0xFF809000)

# get specific bit value:
def getVal(adr=0, pin=0, pinStart=None):
  if (pinStart == None):
    return bin(buffer(region, adr * 4).value)[2:][::-1][(pin):(pin)+1][::-1]
  elif (type(pinStart) is int and pinStart < pin):
    return bin(buffer(region, adr * 4).value)[2:][::-1][(pinStart):(pin)+1][::-1]

def rolAdrs(stackAdr, pin=32, pinStart=0):
  for adr in range(stackAdr):
    print(f"Address {hex(adr*4)} {getVal(adr, pin, pinStart)}")

#memoryview(region).hex()
#buffer(region, 0 * 4).value ^= (1<<0)
#ptrTest = _cui.pointers(buffer(region,0*4))

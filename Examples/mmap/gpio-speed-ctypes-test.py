#!/bin/python

import time, mmap
from ctypes import c_uint32, pointer

# open the memory region of the gpio we want to play with
with open('/dev/mem', 'r+b') as fd:
  region = mmap.mmap(fd.fileno(), (1024*4), offset=0xFF634000)

# set the real header pin number found on the dev board
pin = 1<<(1-1)

# set pin to gpio mode at register 0x116 ("EN_O" register)
c_uint32.from_buffer(region, 0x116 * 4).value &= ~pin

# set pin without pull-up resistor at register 0x14A ("UP_EN" register)
c_uint32.from_buffer(region, 0x14A * 4).value &= ~pin

# set the register pointer to play with
outpin = pointer(c_uint32.from_buffer(region, 0x117 * 4)).contents

# start the timer
ps = time.process_time()

# toggle the pin out value for 1 milion times
for i in range(1000000):
  outpin.value |= pin # pin set to high / ON
  outpin.value &= ~pin # pin set to low / OFF

# stop the timer
pe = time.process_time()

# print the timer result
print("Total time for ctype loop: ", round(pe-ps, 3))



# few comments on basic read & write how to with ctypes
#  #read
#  ctypes.c_uint32.from_buffer(region, (offset*4)).value
#
#  test = ctypes.c_uint32.from_buffer(region, (offset*4)).value ^ (1<<2)
#
#  #write
#  ctypes.c_uint32.from_buffer(region, (offset*4)).value = test

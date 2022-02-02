#!/bin/python

import time, mmap, ctypes

with open('/dev/mem', 'r+b') as fd:
  region = mmap.mmap(fd.fileno(), (1024*4), offset=0xFF634000)

ctypes.c_uint32.from_buffer(region, 0x116 * 4).value = 0
ctypes.c_uint32.from_buffer(region, 0x14A * 4).value = 0

pin = ctypes.c_uint32.from_buffer(region, 0x117 * 4)
pof = 0
pon = 1

ps = time.process_time()

for i in range(1000000):
  pin.value = pof
  pin.value = pon

pe = time.process_time()

print("Total time for ctype loop: ", round(pe-ps, 3))



#CTYPES
#  #read
#  ctypes.c_uint32.from_buffer(region, (offset*4)).value
#
#  test = ctypes.c_uint32.from_buffer(region, (offset*4)).value ^ (1<<2)
#
#  #write
#  ctypes.c_uint32.from_buffer(region, (offset*4)).value = test

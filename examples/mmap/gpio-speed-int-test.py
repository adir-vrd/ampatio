#!/bin/python

import time, mmap

with open('/dev/mem', 'r+b') as fd:
  region = mmap.mmap(fd.fileno(), (1024*4), offset=0xFF634000)

region[4*0x116:4*0x116+4] = b'\x00\x00\x00\x00'
region[4*0x14A:4*0x14A+4] = b'\x00\x00\x00\x00'

pof = (0).to_bytes(4, 'little')
pon = (1).to_bytes(4, 'little')

ps = time.process_time()

for i in range(1000000):
  region[4*0x117:4*0x117+4] = pof
  region[4*0x117:4*0x117+4] = pon

pe = time.process_time()

print("Total time for int loop: ", round(pe-ps, 3))



#INT
#  #read
#  int.from_bytes(region[4*offset:4*offset+4], byteorder='little', signed=False)
#
#  test = (int.from_bytes(region[4*offset:4*offset+4], byteorder='little', signed=False) ^ (1<<2)).to_bytes(4, 'little')
#
#  #write
#  region[4*offset:4*offset+4] = test

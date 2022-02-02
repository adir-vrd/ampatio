#!/bin/python

import time, mmap, struct

with open('/dev/mem', 'r+b') as fd:
  region = mmap.mmap(fd.fileno(), (1024*4), offset=0xFF634000)

region[4*0x116:4*0x116+4] = struct.pack("<L", 0)
region[4*0x14A:4*0x14A+4] = struct.pack("<L", 0)

pof = struct.pack("<L", 0)
pon = struct.pack("<L", 1)

ps = time.process_time()

for i in range(1000000):
  region[4*0x117:4*0x117+4] = pof
  region[4*0x117:4*0x117+4] = pon

pe = time.process_time()

print("Total time for struct loop: ", round(pe-ps, 3))





#STRUCT
#  #read
#  struct.unpack("<L", self.region[4*offset:4*offset+4])[0]
#
#  test = struct.unpack("<L", self.region[4*offset:4*offset+4])[0]
#
#  #write
#  region[4*offset:4*offset+4] = struct.pack("<L", test ^ (1<<2))

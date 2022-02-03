#!/bin/python

""" this is unfinish simple driver for the AM2302 DHT sensor
    in hope to finish it some day...
"""

# import the built in time module for the timer
from time import sleep as delay
from time import monotonic as stamp
from ctypes import c_uint8 as eight

# import the AMPatio lib as amp
import AMPatio as amp

# get & set the board file name from AMPatio/boards folder
# my board is Odroid C4 Rev1 so . . . what's yours?
C4 = amp.board('Odroid_C4')
amp.gpio.Setup(C4)

data_list = []
text_list = []

# humidity temperature sensor data pin set & as high
DHT = amp.gpio.Pin(16, False, 1, 0)

#### set the mask if we want to read mmap directly
#msk = eight(1<<(DHT.bit%8)).value
##
#if DHT.bit < 8:
#  byte = 0
#elif DHT.bit < 16:
#  byte = 1
#elif DHT.bit < 24:
#  byte = 2
#elif DHT.bit < 32:
#  byte = 3
##
#ofs = (4*amp.gpio.device.offsets[DHT.reg]['I'])+byte
####

# simple delay befor we start talking to the sensor
delay(0.1)

# signaling the sensor to get data ready for us
DHT.off()
delay(1000/1000000)

# open line for input from the sensor
DHT.on()
DHT.pull_up()
DHT.pull_on()

# start of data capture proccess
ps = stamp()
while (stamp()-ps) < 0.005:
  data_list.append(DHT.level())

#   alternativ option is to read mmap directly for faster response:
#  data_list.append(amp.gpio.region[ofs] & msk)

#   or we can just do that:
#  data_list.append(amp.gpio.region[ofs] >> DHT.bit & 1)

# close data line
DHT.pull_off()
DHT.off()

#for level in data_list:
#  text_list.append(str(data_list[level]))

# convert 1 to low and 0 to high
for level in data_list:
  if data_list[level] == 1:
    text_list.append('0')
  else:
    text_list.append('1')

# convert it to a single joind string
data_text = ''.join(text_list)

# print the integer value list
print(f"recived data: {data_text} recived length {len(data_text)}")

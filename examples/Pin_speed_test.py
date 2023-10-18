#!/bin/python

# import the built in time module for the timer
import time

# import the AMPatio lib as amp
import AMPatio as amp

# get & set the board file name from AMPatio/boards folder
# my board is Odroid C4 Rev1 so . . . what's yours?
C4 = amp.board_loads('Odroid_C4')
amp.gpio.Setup(C4)

# set the pin
# will test pin number 16 from the 40 pins header found on the Odroid C4 board
tpin = amp.gpio.Pin(18, 2, 1, 3)

PS = time.process_time() # Start write read loop timer

# Do a 1 milion loops with read-write to the pin
for i in range(1000000):
  tpin.on()
  tpin.off()

PE = time.process_time() # End write read loop timer

# print the loops timers
print("Total time write read functions loop: ", round(PE-PS, 3))

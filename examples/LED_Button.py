#!/bin/python

from time import sleep as delay

# import the AMPatio lib as amp
import AMPatio as amp

# get & set the board file name from AMPatio/boards folder
# my board is Odroid C4 Rev1 so . . . what's yours?
C4 = amp.board_loads('Odroid_C4')
amp.gpio.Setup(C4)

# set the LED
LED = amp.gpio.LED(18)

# set a button input (pre made as high level and pull up resistor)
BTN = amp.gpio.BTN(16)

# just a simple loop test until the button is pressed
while 1:
  if BTN.level() == 0: # 0 = low level (when the button is pressd)
    LED.on()
    delay(2) # wait 1 sec
    break

LED.off()

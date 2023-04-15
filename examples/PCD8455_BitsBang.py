#!/usr/bin/env python

# this bitbang modified example made originaly by Henning Aust
# (github.com/HenningAust/py_LCD) for the A20 chip.
#
# this modified version is faster than my previous one.
#
# the original module i test it is PCD8544 Pi hat that fit my Odroid C4
#

# import AMPatio & time.sleep as delay
import AMPatio as amp
from time import sleep as delay

# get & set the board file name from AMPatio/boards folder
# my board is Odroid C4 Rev1 so . . . what's yours?
C4 = amp.board_loads('Odroid_C4')
amp.gpio.Setup(C4)

# set the soft SPI pins on the Odroid C4 board
CLK = amp.gpio.Pin(11) # GPIO_X 3  # SPI-Clock
DIN = amp.gpio.Pin(12) # GPIO_X 16 # SPI-Data
DC  = amp.gpio.Pin(13) # GPIO_X 4  # The Data OR Command set pin
CE  = amp.gpio.Pin(15) # GPIO_X 7  # SPI-CS
RES = amp.gpio.Pin(16) # GPIO_X 0  # Reset

# Constants parameters
X_RANGE = 84
Y_RANGE = 48
LCD_CONTRAST = 0xC0
LCD_SIZE = int(X_RANGE*Y_RANGE/8)
LCD_MEMORY = [0 for i in range(LCD_SIZE)]
#LCD_TEMP = [0 for i in range(X_RANGE)],[0 for i in range(Y_RANGE)]

# SPI function
def send(bytes):
  CE.off()
  i = 0
  for i in range(1,9):
    if (bytes & 0x80):
      DIN.on()
		else:
  		DIN.off()
    #delay(0.00001)
  	CLK.off()
    #delay(0.00001)
  	CLK.on()
  	bytes = bytes << 1
  CE.on()
  #return

# LCD functions
def command(cmd):
	DC.off()
	send(cmd)

def contrast(level):
	command(0x21)
	command(0x14)
	command(level)
	command(0x20)
	command(0x0C)

def clear():
	for i in range(len(LCD_MEMORY)):
			LCD_MEMORY[i]=0

def update(x=0,y=0):
	for y in range(0,int(Y_RANGE/8)):
		command(0x80)
		command(0x40 | (y+1))
    DC.on() # Set DC pin to on before sending data to the display row
		for x in range(X_RANGE):
			send(LCD_MEMORY[y*X_RANGE + x])

def reset():
	CE.on()
	RES.off()
	delay(1)
	RES.on()
	delay(1)
	command(0x21)
	command(0xC8)
	command(0x04)
	command(0x40)
	command(0x12)
	command(0xE4) # Set Display offset line 1
	command(0x45) # Set Display offset line 2: shiftet 5  pixels up and then use lines 1 to 6
	command(0x20)
	command(0x08)
	command(0x0C)
	contrast(LCD_CONTRAST)
	clear()
	update()

# CGI functions
def drawPoint(x,y):
	row = int(y/8)
	i = x + row * 84
	LCD_MEMORY[i] |= 1 << (y % 8)

def drawLine(x1,y1,x2,y2):
	dx=abs(x2-x1)
	dy=abs(y2-y1)
	if(x1 < x2):
	  sx=1
	else:
	  sx=-1
	if(y1 < y2):
	  sy=1
	else:
	  sy=-1
	err=dx-dy
	while(1):
		drawPoint(x1,y1)
		if((x1==x2) & (y1==y2)):
			break
		e2 = 2*err
		if(e2 > -dy):
			err = err-dy
			x1 = x1+sx
		if(e2 < dx):
			err=err+dx
			y1=y1+sy

def drawRect(x1,y1,x2,y2):
	drawLine(x1,y1,x1,y2)
	drawLine(x1,y1,x2,y1)
	drawLine(x2,y1,x2,y2)
	drawLine(x1,y2,x2,y2)






# Drawing test...
from time import process_time as prst
reset()
delay(2)
PS = prst()
for i in range(10):
  pnt = i
  drawRect(pnt,pnt,pnt+8,pnt+8)
  update()
  clear()
  drawRect(pnt,pnt,pnt+8,pnt+8)
  update()
  clear()
  drawRect(pnt,pnt,pnt+8,pnt+8)
  update()
  clear()
  drawRect(pnt,pnt,pnt+8,pnt+8)
  update()
  clear()
PE = prst()
print("Total time to draw: ", round(PE-PS, 3))

#!/usr/bin/env python

# this bitbang modified example made originaly by Henning Aust
# (github.com/HenningAust/py_LCD) for the A20 chip.
#
# the original module i test it is PCD8544 Pi hat that fit my Odroid C4
#


# import the built in time module for the timer
from time import process_time as prst
from time import sleep as delay

# import the AMPatio lib as amp
import AMPatio as amp

# get & set the board file name from AMPatio/boards folder
# my board is Odroid C4 Rev1 so . . . what's yours?
C4 = amp.boards('Odroid_C4')
amp.gpio.Setup(C4)

# set the soft SPI pins on the Odroid C4 board
CLK = amp.gpio.Pin(11) # GPIO_X 3
DIN = amp.gpio.Pin(12) # GPIO_X 16
DC  = amp.gpio.Pin(13) # GPIO_X 4
CS  = amp.gpio.Pin(15) # GPIO_X 7
RST = amp.gpio.Pin(16) # GPIO_X 0

# Some constants / parameter
SEND_CHR = 1
SEND_CMD = 2
X_RANGE = 84
Y_RANGE = 48
DEFAULT_CONTRAST = 0xC0
LCD_CACHE_SIZE = int(X_RANGE*Y_RANGE/8)
LCD_Memory = [0 for i in range(LCD_CACHE_SIZE)]
LCD_TEMP = [0 for i in range(X_RANGE)],[0 for i in range(Y_RANGE)]

def send(cmd,type):
	CS.off()
	if(type == SEND_CHR):
		DC.on()
	else:
		DC.off()
	SPIsendByte(cmd)
	CS.on()


def SPIsendByte(byteTosend):
	i = 0
	for i in range(1,9):
		if (byteTosend & 0x80):
			DIN.on()
		else:
			DIN.off()
		#delay(0.00001)
		CLK.off()
		#delay(0.00001)
		CLK.on()
		byteTosend = byteTosend << 1
	return

def update():
	x = 0
	y = 0
	for y in range(0,int(Y_RANGE/8)):
		send(0x80,SEND_CMD)
#		send(0x40 | y, SEND_CMD)
		send(0x40 | (y+1), SEND_CMD)
		for x in range(X_RANGE):
			send(LCD_Memory[y*X_RANGE + x],SEND_CHR)

def clear():
	for i in range(len(LCD_Memory)):
			LCD_Memory[i]=0

def drawPoint(x,y):
	row = int(y/8)
	i = x + row * 84
	LCD_Memory[i] |= 1 << (y % 8)

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

def setContrast(contrast):
	send(0x21,SEND_CMD)
	send(0x14,SEND_CMD)
	send(contrast,SEND_CMD)
	send(0x20,SEND_CMD)
	send(0x0C,SEND_CMD)

# Reset LCD
def init():
	# SET CS HIGH
	CS.on()
	#Reset LCD
	RST.off()
	delay(1)
	RST.on()
	delay(1)
	send(0x21,SEND_CMD)
	send(0xC8,SEND_CMD)
	send(0x04,SEND_CMD)
	send(0x40,SEND_CMD)
	send(0x12,SEND_CMD)
	send(0xE4,SEND_CMD) # Set Display offset line 1
	send(0x45,SEND_CMD) # Set Display offset line 2: shiftet 5  pixels up and then use lines 1 to 6
	send(0x20,SEND_CMD)
	send(0x08,SEND_CMD)
	send(0x0C,SEND_CMD)
	setContrast(DEFAULT_CONTRAST)
	clear()
	update()


# Draw!
init()
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

clear()

PE = prst()

print("Total time to draw: ", round(PE-PS, 3))

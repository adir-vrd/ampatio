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
DAT = amp.gpio.Pin(12) # GPIO_X 16 # SPI-MOSI
DOC = amp.gpio.Pin(13) # GPIO_X 4  # The Data OR Command set pin
CS  = amp.gpio.Pin(15) # GPIO_X 7  # SPI-CS
RES = amp.gpio.Pin(16) # GPIO_X 0  # Reset

# Constants parameters
X_RANGE = 84
Y_RANGE = 48
LCD_CONTRAST = 0xC0
LCD_SIZE = int(X_RANGE*Y_RANGE/8)
LCD_MEMORY = [0 for i in range(LCD_SIZE)]


# SPI function
def send(data, i=0):
  for i in range(1,9):
    DAT.on() if (data & 0x80) else DAT.off()
    CLK.off()
    CLK.on()
    data = data << 1
  return


# LCD functions
def command(data, char=False):
  CS.off()
  DOC.on() if char else DOC.off()
  send(data)
  CS.on()

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
    command(0x40|(y+1))
    for x in range(X_RANGE):
      command(LCD_MEMORY[y*X_RANGE+x], False)

def reset():
  CS.on()
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
reset()
drawLine(1,1,80,40)
update()

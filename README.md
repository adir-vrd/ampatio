# AMPatio
Clean & pure Python library for controlling & manipulate digital IO pins on Amlogic SoC based boards.

this library only in it's diapers and allready make it simple to use python for accessing
AMLogic based socs low level perpherals in linux.

for How-To access the GPIO take a fast look at the examples folder.

Importent! this module/liberary can only be run only as root user!
since linux /dev/mem can be only accessd and manipulated as root only.



## 2-Do
gpio:
- move from importlib to pkgutil
- add occupied and release pin functions (by recording json file in /tmp folder)
- add functions to do buffer read & write
- add relevant "dungen" functions

**irb/ird: (Infra-Red Blaster/Decoder)**
- for now meson IR modules are removable in mainline kernel (Archlinux-AARCH64) but not implemented yet here.
  also need to set MUX (a.k.a. Alternative Function) before use.
  available only with "A311D, S905D3, S905X3, S922X" SOCs based boards. (WIP)

### 2-Do Major note
Most of the hardware that will be present soon in the examples folder will used to pass data by BitBang method only for now.
To use "SPI/IIC/UART/ADC/PWM" we need to set those meson modules in the kernel as dynamically loaded.
To do so, it's require from us to recompile the Linux kernel, but until i would do so i wrote only the GPIO part.
(also look at /sys/devices/platform/soc)



## Performence

The test is simply driving a selected Pin to on & off state a million times.
which result in 4.582 Seconds, Not bad at all for the slowly snake we play with :)

Importent! i did test my lib only on my Odroid C4 board.

The speed test file located in the examples folder.
Don't forget to change the board model & pin number to match your case before you run it!



## License & CopyRights

AMPatio is made by Adir Vered with ISC License.

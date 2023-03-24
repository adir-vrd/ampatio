#  ISC
#
#  Copyright (c) 2022 Adir Vered <adir.vrd@gmail.com>
#
#  Permission to use, copy, modify, and/or distribute this software for any purpose
#  with or without fee is hereby granted, provided that the above copyright notice
#  and this permission notice appear in all copies.
#
#  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
#  REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
#  AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
#  INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
#  LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
#  OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE
#  OR PERFORMANCE OF THIS SOFTWARE.


address = [
  # GPIO_A/BOOT/C/DIF/H/X/Y/Z/...:
  # we need to substruct 0x400 from the original offset then we add 0x100
  # to all mentiond above registers offsets in this region.
  # by the datasheet we need to multipile the offset by 4 and there for
  # the offset for each register is get the 0x400 missing, got it?!
  0xFF634000, # GPIO (0xFF634400 - 0x400)
  0xFF800000  # GPIO_AO
  ]

offsets = {
  # GPIO_AO
  "AO" : {
    "O_EN"  : 0x09,
    "O"     : 0x0D,
    "I"     : 0x0A,
    "UP"    : 0x0B,
    "UP_EN" : 0x0C,
    #"DS_0A" : 0x07,
    #"DS_0B" : 0x08,
    #"MUX_0" : 0x05,
    #"MUX_1" : 0x06
    },
  # GPIO_BOOT (REG_0)
  "BOOT" : {
    "O_EN"  : 0x110,
    "O"     : 0x111,
    "I"     : 0x112,
    "UP"    : 0x13A,
    "UP_EN" : 0x148,
    #"DS_0A" : 0x1D0,
    #"MUX_0" : 0x1B0,
    #"MUX_1" : 0x1B1
    },
  # GPIO_C (REG_1)
  "C" : {
    "O_EN"  : 0x113,
    "O"     : 0x114,
    "I"     : 0x115,
    "UP"    : 0x13B,
    "UP_EN" : 0x149,
    #"DS_1A" : 0x1D1,
    #"MUX_9" : 0x1B9
    },
  # GPIO_X (REG_2)
  "X" : {
    "O_EN"  : 0x116,
    "O"     : 0x117,
    "I"     : 0x118,
    "UP"    : 0x13C,
    "UP_EN" : 0x14A,
    #"DS_2A" : 0x1D2,
    #"DS_2B" : 0x1D3,
    #"MUX_3" : 0x1B3,
    #"MUX_4" : 0x1B4,
    #"MUX_5" : 0x1B5
    },
  # GPIO_H (REG_3)
  "H" : {
    "O_EN"  : 0x119,
    "O"     : 0x11A,
    "I"     : 0x11B,
    "UP"    : 0x13D,
    "UP_EN" : 0x14B,
    #"DS_3A" : 0x1D4,
    #"MUX_B" : 0x1BB,
    #"MUX_C" : 0x1BC
    },
  # GPIO_Z (REG_4)
  "Z" : {
    "O_EN"  : 0x11C,
    "O"     : 0x11D,
    "I"     : 0x11E,
    "UP"    : 0x13E,
    "UP_EN" : 0x14C,
    #"DS_4A" : 0x1D5,
    #"MUX_6" : 0x1B6,
    #"MUX_7" : 0x1B7
    },
  # GPIO_A (REG_5)
  "A" : {
    "O_EN"  : 0x120,
    "O"     : 0x121,
    "I"     : 0x122,
    "UP"    : 0x13F,
    "UP_EN" : 0x14D,
    #"DS_5A" : 0x1D6,
    #"MUX_D" : 0x1BD,
    #"MUX_E" : 0x1BE
    },
  }

presets = {
  # Need to confirm ! GPIO_H: {"UP"/"UP_EN"} start @ bit 4 ?
  }

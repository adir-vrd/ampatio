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
  0xC8834000,
  # GPIO_AO:
  0xC8100000
  ]

offsets = {
  # GPIO_AO
  "AO" : {
    "O_EN"  : 0x09,
    "O"     : 0x09,
    "I"     : 0x0A,
    "UP"    : 0x0B,
    "UP_EN" : 0x0B
    },
  # GPIO_Z
  "Z" : {
    "O_EN"  : 0x115,
    "O"     : 0x116,
    "I"     : 0x117,
    "UP"    : 0x13D,
    "UP_EN" : 0x14B
    },
  # GPIO_CLK
  "CLK" : {
    "O_EN"  : 0x115,
    "O"     : 0x116,
    "I"     : 0x117,
    "UP"    : 0x13D,
    "UP_EN" : 0x14B
    },
  # GPIO_CARD
  "CARD" : {
    "O_EN"  : 0x112,
    "O"     : 0x113,
    "I"     : 0x114,
    "UP"    : 0x13C,
    "UP_EN" : 0x14A
    },
  # GPIO_BOOT
  "BOOT" : {
    "O_EN"  : 0x112,
    "O"     : 0x113,
    "I"     : 0x114,
    "UP"    : 0x13C,
    "UP_EN" : 0x14A
    },
  # GPIO_H
  "H" : {
    "O_EN"  : 0x10F,
    "O"     : 0x110,
    "I"     : 0x111,
    "UP"    : 0x13B,
    "UP_EN" : 0x149
    },
  # GPIO_Y
  "Y" : {
    "O_EN"  : 0x10F,
    "O"     : 0x110,
    "I"     : 0x111,
    "UP"    : 0x13B,
    "UP_EN" : 0x149
    },
  # GPIO_DV
  "DV" : {
    "O_EN"  : 0x10C,
    "O"     : 0x10D,
    "I"     : 0x10E,
    "UP"    : 0x13A,
    "UP_EN" : 0x148
    },
  # GPIO_X
  "X" : {
    "O_EN"  : 0x118,
    "O"     : 0x119,
    "I"     : 0x11A,
    "UP"    : 0x13E,
    "UP_EN" : 0x14C
    },
  }

presets = {
  # offsets pre shift bit:
  "AO" : {
    "O"     : 16,
    "UP"    : 16
    },
  "Z" : {
    "O_EN"  : 14,
    "O"     : 14,
    "I"     : 14,
    "UP"    : 14,
    "UP_EN" : 14
    },
  "CLK" : {
    "O_EN"  : 28,
    "O"     : 28,
    "I"     : 28,
    "UP"    : 28,
    "UP_EN" : 28
    },
  "CARD" : {
    "O_EN"  : 20,
    "O"     : 20,
    "I"     : 20,
    "UP"    : 20,
    "UP_EN" : 20
    },
  "H" : {
    "O_EN"  : 20,
    "O"     : 20,
    "I"     : 20,
    "UP"    : 20,
    "UP_EN" : 20
    }
  }

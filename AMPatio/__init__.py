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


import json as _json
from importlib import resources as _il_res

#__all__ = [ "gpio", "spi", "iic", "uart", "pwm", "irb", "ird", "adc" ]

from . import gpio
#from . import spi
#from . import iic
#from . import uart
#from . import ir
#from . import pwm
#from . import adc

from . import boards

# board selector function:
board_loads = lambda _brd: _json.load(open(_il_res.path(boards, _brd+".json"), "r"))

""" AMPatio
    Clean & pure Python module for direct perpherals access & manipulation
    by using mamp & Linux /dev/mem interface for the AMLogic SoC family.

    Made by Adir Vered.

    adir-vrd@github
    adir-vrd@linkdin

    ISC License
"""

import json as _json

#__all__ = [ "gpio", "spi", "iic", "uart", "pwm", "irb", "ird", "adc" ]

from . import gpio
#from . import spi
#from . import iic
#from . import uart
#from . import ir
#from . import pwm
#from . import adc

# board selector function:
boards = lambda board: _json.load(open("AMPatio/boards/"+board+".json", "r"))

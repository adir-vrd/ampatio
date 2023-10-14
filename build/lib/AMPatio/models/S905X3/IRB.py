address = [
  0xFF800000
  ]

offsets = {
  "ADDR0" : 0x3,
  "ADDR1" : 0x4,
  "ADDR2" : 0x5,
  "ADDR3" : 0x6
  }

presets = { "ADDR" : [
  { "BUSY" : (1<<26),
    "FIFO_FULL" : (1<<25),
    "FIFO_EMPTY" : (1<<24),
    "FIFO_LEVEL" : (0xff<<16),
    "MODULATOR_TB_SYSTEM_CLOCK" : (0x0<<12),
    "MODULATOR_TB_XTAL3_TICK" : (0x1<<12),
    "MODULATOR_TB_1US_TICK" : (0x2<<12),
    "MODULATOR_TB_10US_TICK" : (0x3<<12),
    "SLOW_CLOCK_DIV" : (0xff<<4),
    "SLOW_CLOCK_MODE" : (1<<3),
    "INIT_HIGH" : (1<<2),
    "INIT_LOW" : (1<<1),
    "ENABLE" : (1<<0)
    },
  { "MODULATION_LOW_COUNT" : lambda x: (x<<16),
    "MODULATION_HIGH_COUNT" : lambda x: (x<<0)
    },
  { "WRITE_FIFO" : (1<<16),
    "MODULATION_ENABLE" : (1<<12),
    "TIMEBASE_1US" : (0x0<<10),
    "TIMEBASE_10US" : (0x1<<10),
    "TIMEBASE_100US" : (0x2<<10),
    "TIMEBASE_MODULATION_CLOCK" : (0x3<<10)
    },
  { "FIFO_THD_PENDING" : (1<<16),
    "FIFO_IRQ_ENABLE" : (1<<8),
    "FIFO_IRQ_THRESHOLD" : lambda x: ((x&0xff)<<0)
    }
  ]}

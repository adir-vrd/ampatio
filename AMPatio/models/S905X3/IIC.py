address = [
  0xFFD1C000, # IIC_3
  0xFFD1D000, # IIC_2
  0xFFD1E000, # IIC_1
  0xFFD1F000, # IIC_0
  0xff806000, # IIC_AO_S ?! i need to be confirm that..
  0xff805000  # IIC_AO
  ]

offsets = {
  "CONTROL_REG"      : 0x0,
  "SLAVE_ADDR"       : 0x1,
  "TOKEN_LIST_REG0"  : 0x2,
  "TOKEN_LIST_REG1"  : 0x3,
  "TOKEN_WDATA_REG0" : 0x4,
  "TOKEN_WDATA_REG1" : 0x5,
  "TOKEN_RDATA_REG0" : 0x6,
  "TOKEN_RDATA_REG1" : 0x7
  }

presets = {}

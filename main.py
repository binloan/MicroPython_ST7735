import ST7735
from machine import SPI, Pin

displayres = 'P7'
displaydc = 'P8'
displaycs = 'P9'
displaysda = 'P11'
displaysck = 'P10'

spi = SPI(0, baudrate=8000000, polarity=0, phase=0)

d = ST7735.ST7735(spi, rst=displayres, ce=displaycs, dc=displaydc)

d.reset()
d.begin()
d.fill_screen(0x0000)
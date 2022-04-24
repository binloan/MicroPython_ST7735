# Display size X: 128 Y:160
import ST7735
import lcd_gfx
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
d.fill_screen(d.rgb_to_565(0,0,0))

x = int(d._width/2)
y = int(d._height/2)
r = int(min(x,y)/2)

lcd_gfx.drawLine(0,0,d._width/2,0,d,d.rgb_to_565(255,255,255))
d.set_rotation(1)
d._bground = d.rgb_to_565(0,0,0)
d._color = d.rgb_to_565(255,255,255)
d.p_string(0,0,'Hello World!')
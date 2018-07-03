import time
import CHIP_IO.GPIO
from luma.core.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544, st7735, uc1701x

serial = spi(port=32766, device=0, gpio=CHIP_IO.GPIO, gpio_DC="CSID1", gpio_RST="CSID0")
device = ss7735(serial)
with canvas(device) as draw:
 draw.rectangle(device.bounding_box, outline="white")
 draw.text((3, 3), "Hello", fill="white")
 
 time.sleep(10)

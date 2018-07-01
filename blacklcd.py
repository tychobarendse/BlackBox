import time
import CHIP_IO.GPIO
from luma.core.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
serial = spi(port=32766, device=0, gpio=CHIP_IO.GPIO, gpio_DC="CSID1", gpio_RST="CSID0")
device = ssd1306(serial)
with canvas(device) as draw:
 draw.rectangle(device.bounding_box, outline="white")
 draw.text((3, 3), "Hello", fill="white")
 
 time.sleep(10)
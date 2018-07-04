from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544, st7735, uc1701x

serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=24)
device = pcd8544(serial)

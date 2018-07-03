import CHIP_IO.GPIO
from luma.core.serial import spi
from luma.oled.device import ssd1306

#Replace device = cmdline.create_device(args) with

serial = spi(port=32766, device=0, gpio=CHIP_IO.GPIO, bcm_DC=“CSID1”, bcm_RST=“CSID0”)
device = ssd1306(serial)

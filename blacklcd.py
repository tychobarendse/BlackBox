import time
import CHIP_IO.GPIO
import os.path
from PIL import Image
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544, st7735, uc1701x

img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'starwars.png'))
serial = spi(port=32766, device=0, gpio=CHIP_IO.GPIO, gpio_DC="CSID1", gpio_RST="CSID0")
device = st7735(serial)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 40), "Hello World", fill="red")
time.sleep(10)
 
# open photo
photo = Image.open(img_path).convert("RGBA")
# display on screen for a few seconds
device.display(photo.convert(device.mode))
time.sleep(10)

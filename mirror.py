import time
import CHIP_IO.GPIO
import os.path
import pyscreenshot as ImageGrab
from PIL import Image
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import pcd8544, st7735, uc1701x

img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'PAL.png'))
serial = spi(port=32766, device=0, gpio=CHIP_IO.GPIO, gpio_DC="CSID1", gpio_RST="CSID0")
device = st7735(serial)

'''
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 40), "Hello World", fill="red")
time.sleep(1)
''' 

logo = Image.open(img_path).convert("RGBA").resize(device.size)
#img = Image.new(logo.mode, logo.size, (255,) * 4)

background = Image.new("RGBA", device.size, "black")
posn = ((device.width - logo.width) // 2, 0)
background.paste(logo, posn)
device.display(background.convert(device.mode))
time.sleep(5)


#background = Image.new("RGBA", device.size, "black")
while True:
 im = ImageGrab.grab().convert("RGBA").resize(device.size)
 #posn = ((device.width - im.width) // 2, 0)
 #background.paste(im, posn)
 #device.display(background.convert(device.mode))
 device.display(im.convert(device.mode))



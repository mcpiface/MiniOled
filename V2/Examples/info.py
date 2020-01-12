# Copyright (c) 2017 Adafruit Industries
# Author: Tony DiCola & James DeVito
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

# See: http://effbot.org/imagingbook/imagedraw.htm
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess
import os

# Raspberry Pi pin configuration:
RST = None     

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
#font = ImageFont.load_default()
font = ImageFont.truetype("arial.ttf", 15)
font = ImageFont.truetype("/usr/share/fonts/truetype/gentium/Gentium-R.ttf", 28)
small_font = ImageFont.truetype("/usr/share/fonts/truetype/gentium/Gentium-R.ttf", 20)

def read_pi_temperature():
    temperature = os.popen("vcgencmd measure_temp").readline()
    return temperature.replace("temp=","")

item_to_show = 0;

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )

    cmd = "hostname | cut -d\' \' -f1"
    Hostname = subprocess.check_output(cmd, shell = True )

    cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )

    if item_to_show==0:
        draw.text((x, top), "IP: " + str(IP),  font=font, fill=255)
    else if item_to_show == 1:
        draw.text((x, top+8), str(CPU), font=font, fill=255)
    else if item_to_show == 2:
        draw.text((x, top+16), Hostname,  font=font, fill=255)
    elif item_to_show == 3:
        temperature = read_pi_temperature()
        draw.text((x,top), temperature, font=font, fill=255)


    # Display image.
    disp.image(image)
    disp.display()

    time.sleep(1)

    item_to_show++

    if item_to_show > 3:
	item_to_show = 0
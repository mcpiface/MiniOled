# MiniOled


## Python setup

sudo apt-get update
sudo apt-get install build-essential python-dev python-pip
sudo pip install RPi.GPIO


/// ----------------------------
Didn't do:

sudo apt-get install python-imaging python-smbus

sudo apt-get install git
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install
/// ----------------------------

SSD1306 Driver from Adafruit:

https://github.com/adafruit/Adafruit_Python_SSD1306

sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install Adafruit-SSD1306


--

Demo:

git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306/examples/stats.py

----------------

Check for I2C display:
sudo apt-get install i2c-tools
sudo i2cdetect -y 1

Expect address: 3c
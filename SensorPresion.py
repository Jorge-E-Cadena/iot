from machine import Pin, I2C
from time import sleep_ms
from ssd1306 import SSD1306_I2C
import bme280
import framebuf

WIDTH = 128
HEIGHT = 64
i2c = I2C(1, scl=Pin(9), sda=Pin(10))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
bme = bme280.BME280(i2c=i2c)

while True:
    print(bme.values())
    sleep_ms(500)
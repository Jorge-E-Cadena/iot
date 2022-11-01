from machine import Pin, I2C
from time import sleep_ms
from ssd1306 import SSD1306_I2C
import bme280
import framebuf


ANCHO = 128
ALTO =64
i2c = I2C(1, scl=Pin(19), sda=Pin(18))
oled = SSD1306_I2C(ANCHO,ALTO, i2c)
bme = bme280.BME280(i2c=i2c)
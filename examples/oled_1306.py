from machine import Pin, I2C
from ssd1306 import SSD1306_I2C # type: ignore
from time import sleep
import math

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

radius = 30
x_center = 64
y_center = 32
phase = 0

# Figura de Lissajous
while True:
    for degree in range(0, 360, 1):
        rads = math.radians(degree)
        x = int(x_center + math.cos(3*rads + phase) * radius)
        y = int(y_center + math.sin(5*rads) * radius)
        oled.pixel(x, y, 1)
    oled.show()
    oled.fill(0)
    phase = phase + 2*math.pi/360

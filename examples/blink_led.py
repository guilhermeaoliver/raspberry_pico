from machine import Pin
from time import sleep

red_led = Pin(15,Pin.OUT)

while True:
    red_led.toggle()
    sleep(1)

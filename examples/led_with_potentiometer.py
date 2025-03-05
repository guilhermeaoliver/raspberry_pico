from machine import Pin, ADC
from time import sleep

green_led = Pin(2, Pin.OUT)
yellow_led = Pin(3, Pin.OUT)
red_led = Pin(4, Pin.OUT)
pot = ADC(28)

while True:
    pot_val = pot.read_u16()
    voltage = (pot_val / 65535) * 3.3
    print(voltage)
    
    if voltage <= 1.1:
        green_led.value(1)
        yellow_led.value(0)
        red_led.value(0)

    elif voltage <= 2.2:
        green_led.value(0)
        yellow_led.value(1)
        red_led.value(0)
    
    elif voltage <= 3.3:
        green_led.value(0)
        yellow_led.value(0)
        red_led.value(1)

    sleep(0.5)
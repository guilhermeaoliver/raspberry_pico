from machine import Pin
from time import sleep

red_led_1 = Pin(13, Pin.OUT)
red_led_2 = Pin(12, Pin.OUT)
red_led_3 = Pin(11, Pin.OUT)
red_led_4 = Pin(10, Pin.OUT)

while True:
    # 0
    red_led_1.value(0)
    red_led_2.value(0)
    red_led_3.value(0)
    red_led_4.value(0)
    sleep(1)
    
    # 1
    red_led_1.value(0)
    red_led_2.value(0)
    red_led_3.value(0)
    red_led_4.value(1)
    sleep(1)

    # 2
    red_led_1.value(0)
    red_led_2.value(0)
    red_led_3.value(1)
    red_led_4.value(0)
    sleep(1)

    # 3
    red_led_1.value(0)
    red_led_2.value(0)
    red_led_3.value(1)
    red_led_4.value(1)
    sleep(1)

    # 4
    red_led_1.value(0)
    red_led_2.value(1)
    red_led_3.value(0)
    red_led_4.value(0)
    sleep(1)

    # 5
    red_led_1.value(0)
    red_led_2.value(1)
    red_led_3.value(0)
    red_led_4.value(1)
    sleep(1)

    # 6
    red_led_1.value(0)
    red_led_2.value(1)
    red_led_3.value(1)
    red_led_4.value(0)
    sleep(1)

    # 7
    red_led_1.value(0)
    red_led_2.value(1)
    red_led_3.value(1)
    red_led_4.value(1)
    sleep(1)

    # 8
    red_led_1.value(1)
    red_led_2.value(0)
    red_led_3.value(0)
    red_led_4.value(0)
    sleep(1)

    # 9
    red_led_1.value(1)
    red_led_2.value(0)
    red_led_3.value(0)
    red_led_4.value(1)
    sleep(1)

    # 10
    red_led_1.value(1)
    red_led_2.value(0)
    red_led_3.value(1)
    red_led_4.value(0)
    sleep(1)

    # 11
    red_led_1.value(1)
    red_led_2.value(0)
    red_led_3.value(1)
    red_led_4.value(1)
    sleep(1)

    # 12
    red_led_1.value(1)
    red_led_2.value(1)
    red_led_3.value(0)
    red_led_4.value(0)
    sleep(1)

    # 13
    red_led_1.value(1)
    red_led_2.value(1)
    red_led_3.value(0)
    red_led_4.value(1)
    sleep(1)

    # 14
    red_led_1.value(1)
    red_led_2.value(1)
    red_led_3.value(1)
    red_led_4.value(0)
    sleep(1)

    # 15
    red_led_1.value(1)
    red_led_2.value(1)
    red_led_3.value(1)
    red_led_4.value(1)
    sleep(1)
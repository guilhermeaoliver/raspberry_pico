from machine import PWM, Pin
from time import sleep

analogOut=PWM(Pin(16))
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
    voltage = float(input("What voltage would you like? "))
    pwm_value = (65535/3.3) * voltage
    analogOut.duty_u16(int(pwm_value))
    sleep(.1)
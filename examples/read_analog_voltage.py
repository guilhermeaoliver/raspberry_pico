import machine
from time import sleep

pot_pin = 28
pot = machine.ADC(pot_pin)

while True:
    pot_val = pot.read_u16()
    voltage = (pot_val/65535) * 3.3 
    print(voltage)
    sleep(.5)
from imu import MPU6050  # type: ignore
from machine import I2C, Pin
from time import sleep

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
mpu = MPU6050(i2c)

while True:
    ax = mpu.accel.x
    ay = mpu.accel.y
    az = mpu.accel.z - 0.02203194 * mpu.accel.z - 0.4627616

    print("ax={:.4f}\tay={:.4f}\taz={:.4f}".format(ax, ay, az))
    sleep(.5)

from imu import MPU6050  # type: ignore
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
mpu = MPU6050(i2c)

while True:
    x_accel = mpu.accel.x
    y_accel = mpu.accel.y
    z_accel = mpu.accel.z

    print("Acceleration: x={:.2f} y={:.2f} z={:.2f}".format(x_accel, y_accel, z_accel))
    time.sleep(.5)

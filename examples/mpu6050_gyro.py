from imu import MPU6050  # type: ignore
from machine import I2C, Pin
from time import sleep

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
mpu = MPU6050(i2c)

while True:
    gx = mpu.gyro.x - 0.2535046
    gy = mpu.gyro.y + 2.064006
    gz = mpu.gyro.z + 1.710218

    print("gx={:.4f}\tgy={:.4f}\tgz={:.4f}".format(gx, gy, gz))
    sleep(.5)

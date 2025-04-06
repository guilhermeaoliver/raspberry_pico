from imu import MPU6050 # type: ignore
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
mpu = MPU6050(i2c)

print('Estabilizando o MPU por 5 segundos')
time.sleep(5)
print('MPU estabilizado')

def get_gyro():
    gx = mpu.gyro.x
    gy = mpu.gyro.y
    gz = mpu.gyro.z
    return gx, gy, gz

def gyro_calibration(calibration_time=10):
    """
    Função para obter os valores de deslocamento para calibrar o giroscópio do MPU6050.
    Parâmetros:
    calibration_time[int]:
        Tempo em segundos que você deseja calibrar o MPU6050.
        Quanto mais longo o período, mais preciso o resultado.
    Saídas:
        Array com deslocamentos para os três eixos de rotação [offset_gx, offset_gy, offset_gz].
    """

    print('Iniciando a calibração do giroscópio. Não mova o MPU6050')
    offsets = [0, 0, 0]
    num_of_points = 0
    end_loop_time = time.time() + calibration_time

    while end_loop_time > time.time():
        num_of_points += 1
        (gx, gy, gz) = get_gyro()
        offsets [0] += gx
        offsets[1] += gy
        offsets [2] += gz
        if num_of_points % 100 == 0:
            print('Calibrando: %d pontos coletados.' % num_of_points)

    print('Calibração do giroscópio finalizada. %d pontos no total.' % num_of_points)
    offsets = [i/num_of_points for i in offsets]

    return offsets

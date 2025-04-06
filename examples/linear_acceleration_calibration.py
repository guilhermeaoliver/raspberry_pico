from imu import MPU6050 # type: ignore
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
mpu = MPU6050(i2c)

print('Estabilizando o MPU por 5 segundos')
time.sleep(5)
print('MPU estabilizado')

def get_linear_acceleration():
    ax = mpu.accel.x
    ay = mpu.accel.y
    az = mpu.accel.z
    return ax, ay, az

def linear_calibration(calibration_time = 5, axis = 2):
    """
    Função para obter os valores de deslocamento para calibrar a aceleração linear do MPU6050.
    Nesta função calculamos uma linha de melhor ajuste na qual o eixo x é a aceleração e o eixo
    y é o deslocamento. Assumimos que a linha possui um ajuste linear usamos o método dos mínimos
    quadrados para encontrar a inclinação e a interceptação y.
    Parâmetros:
    calibration_time[int]:
        Tempo em segundos que você deseja calibrar o MPU6050.
        Quanto mais longo o período, mais preciso o resultado.
    axis[int]:
        Eixo a ser calibrado. É recomendado fazer para os 3 eixos.
        ax -> 0, ay -> 1, az -> 2.
    Saídas: 
        Valores m e b para a equação: y = (m * x) + b
    """

    num_of_points = 0
    x_sum = 0
    y_sum = 0
    x_squared_sum = 0
    x_times_y_sum = 0

    # Calibração 1 (Aceleração = 1G)
    print('Oriente o eixo para cima contra a gravidade. Clique em Enter quando estiver pronto.' )
    x = input()
    end_loop_time = time.time() + calibration_time
    print('Calibração 1 (Aceleração = 1G) por %d segundos' % calibration_time)
    while end_loop_time > time.time():
        num_of_points += 1
        offset = get_linear_acceleration()[axis] - 1
        x_sum += 1
        y_sum += offset
        x_squared_sum += 1
        x_times_y_sum += 1 * offset
        if num_of_points % 100 == 0:
            print('Calibrando: %d pontos coletados.' % num_of_points)

    # Calibração 2 (Aceleração = -1G)
    print('Oriente o eixo para baixo contra a gravidade. Clique em Enter quando estiver pronto.' )
    x = input()
    end_loop_time = time.time() + calibration_time
    print('Calibração 2 (Aceleração = -1G) por  %d segundos' % calibration_time)
    while end_loop_time > time.time():
        num_of_points += 1
        offset = get_linear_acceleration()[axis] + 1
        x_sum += (-1 * 1)
        y_sum += offset
        x_squared_sum +=(-1*1)*(-1*1)
        x_times_y_sum += (-1*1) * offset
        if num_of_points % 100 == 0:
            print('Calibrando: %d pontos coletados.' % num_of_points)

    # Calibração 3 (Aceleração = 0G)
    print('Oriente o eixo perpendicularmente contra a gravidade. Clique em Enter quando estiver pronto.' )
    x = input()
    end_loop_time = time.time() + calibration_time
    print('Calibração 3 (Aceleração = 0G) por %d segundos' % calibration_time)
    while end_loop_time > time.time():
        num_of_points += 1
        offset = get_linear_acceleration()[axis] + 0
        x_sum += 0
        y_sum += offset
        x_squared_sum += (0) * (0)
        x_times_y_sum += (0) * offset
        if num_of_points % 100 == 0:
            print('Calibrando: %d pontos coletados.' % num_of_points)

    # Método dos mínimos quadrados
    m = (num_of_points * x_times_y_sum - (x_sum * y_sum)) / ((num_of_points*x_squared_sum) -(x_sum) ** 2)
    b = (y_sum - (m * x_sum)) / num_of_points

    return m, b

print(linear_calibration())
import serial
import keyboard
import time

# Inicialización del puerto serial
ser = serial.Serial('COM5', 9600)  # 'COMX' puerto correcto

while True:
    # Lectura de datos desde el puerto serial
    data = ser.readline().decode().strip()
    print("Datos recibidos:", data)

    # Separar los valores de los ejes X e Y
    values = data.split(',')
    xValue = int(values[0].split(':')[1])
    yValue = int(values[1].split(':')[1])

    # Condicionales para asignar teclas según valores del joystick
    
    if yValue < 515:
        keyboard.press_and_release('e')
    elif yValue > 518:
        keyboard.press_and_release('q')

    if xValue < 493:
        keyboard.press_and_release('r')
    elif xValue > 495:
        keyboard.press_and_release('f')

    # Agrega una pausa para evitar una presión continua de teclas
    time.sleep(0.1)

ser.close()

import serial
import time

# Substitua 'COM3' pela porta correta do seu Arduino
porta_serial = 'COM3'  # Altere para a porta correta se necessário

try:
    # Tente abrir a porta serial
    arduino = serial.Serial(porta_serial, 9600, timeout=1)
    print("Porta serial aberta com sucesso!")

    # Aguarde um momento para garantir que a conexão seja estabelecida
    time.sleep(2)

    # Envie um comando "ON" para o Arduino
    arduino.write(b'ON\n')
    print("Comando 'ON' enviado.")

    # Aguarde um momento para ver a resposta
    time.sleep(1)

    # Envie um comando "OFF" para o Arduino
    arduino.write(b'OFF\n')
    print("Comando 'OFF' enviado.")

    # Feche a porta serial
    arduino.close()
    print("Porta serial fechada.")

except serial.SerialException as e:
    print(f"Erro ao abrir a porta: {e}")
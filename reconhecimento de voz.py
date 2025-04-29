import speech_recognition as sr
import serial
import time

# Configura a porta serial (substitua 'COM3' pela porta correta do seu Arduino)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Aguarda a conexão ser estabelecida

# Inicializa o reconhecedor de voz
recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Aguardando comando...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).upper()  # Reconhece o comando
            print(f"Comando recebido: {command}")

            if command == "BABY OFF":
                arduino.write(b'ON\n')  # Envia comando para ligar
            if command == "BABE OFF":
                arduino.write(b'ON\n')  # Envia comando para ligar
            elif command == "BABY POWER":
                arduino.write(b'OFF\n')  # Envia comando para desligar

        except sr.UnknownValueError:
            print("Não entendi o comando.")
        except sr.RequestError as e:
            print(f"Erro ao se conectar ao serviço de reconhecimento de voz: {e}")
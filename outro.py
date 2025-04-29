import speech_recognition as sr
import serial
import time

# Configura a porta serial (substitua 'COM3' pela porta correta do seu Arduino)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Aguarda a conexão ser estabelecida

# Inicializa o reconhecedor de voz
reconhecedor = sr.Recognizer()

try:
    while True:
        with sr.Microphone() as fonte:
            print("Aguardando comando...")
            audio = reconhecedor.listen(fonte)

            try:
                comando = reconhecedor.recognize_google(audio, language='pt-BR').upper()  # Reconhece o comando em português
                print(f"Comando recebido: {comando}")

                if comando == "JOÃO DESLIGA":
                    arduino.write(b'ON\n')  # Envia comando para ligar
                elif comando == "JOÃO LIGA":
                    arduino.write(b'OFF\n')  # Envia comando para desligar
                elif comando == "opa":
                    print("Saindo...")
                    break  # Encerra o loop

            except sr.UnknownValueError:
                print("Não entendi o comando.")
            except sr.RequestError as e:
                print(f"Erro ao se conectar ao serviço de reconhecimento de voz: {e}")

except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")

finally:
    arduino.close()  # Fecha a conexão serial
    print("Conexão serial fechada.")
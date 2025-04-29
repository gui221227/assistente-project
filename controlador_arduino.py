import serial
import time
from flask import Flask, request

# Configura a porta serial (substitua 'COM3' pela porta correta do seu Arduino)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Aguarda a conexão ser estabelecida

app = Flask(__name__)

@app.route("/send_command", methods=["POST"])
def send_command():
    data = request.json
    command = data.get("command")
    
    if command == "ON":
        arduino.write(b'ON\n')  # Envia comando para ligar
        return {"status": "success", "message": "Dispositivo ligado."}
    elif command == "OFF":
        arduino.write(b'OFF\n')  # Envia comando para desligar
        return {"status": "success", "message": "Dispositivo desligado."}
    else:
        return {"status": "error", "message": "Comando desconhecido."}

if __name__ == "__main__":
    app.run(port=5001)  # Execute em uma porta diferente
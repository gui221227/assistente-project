from flask import Flask, render_template_string, request
import serial
import time

# Configura a porta serial (substitua 'COM3' pela porta correta do seu Arduino)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Aguarda a conexão ser estabelecida

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maria - Assistente Virtual</title>
    <script src="https://code.responsivevoice.org/responsivevoice.js?key=QHSAVIts"></script>
    <script>
        let recognition;
        let wakeWord = "maria";
        let mic;
        let listening = false;

        window.onload = function() {
            mic = document.getElementById("mic");
            setupRecognition();
            setTimeout(() => speak("Olá! Eu sou Maria, sua assistente virtual."), 1500);
        };

        function setupRecognition() {
            recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = "pt-BR";
            recognition.continuous = true;
            recognition.interimResults = false;

            recognition.onresult = function(event) {
                let transcript = event.results[event.results.length - 1][0].transcript.toLowerCase().trim();
                console.log("Frase detectada:", transcript);

                if (transcript.includes(wakeWord)) {
                    speak("Sim, estou ouvindo...");
                    updateMic(true);
                    recognition.stop();
                    setTimeout(startCommandRecognition, 1000);
                }
            };

            recognition.onerror = function(event) {
                console.error("Erro no reconhecimento:", event.error);
            };

            recognition.onend = function() {
                if (!listening) recognition.start();
            };

            recognition.start();
            updateMic(false);
        }

        function startCommandRecognition() {
            let commandRecognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            commandRecognition.lang = "pt-BR";
            commandRecognition.interimResults = false;
            commandRecognition.maxAlternatives = 1;

            listening = true;
            updateMic(true);
            
            commandRecognition.onresult = function(event) {
                let command = event.results[0][0].transcript.toLowerCase().trim();
                console.log("Comando reconhecido:", command);
                document.getElementById("content").innerText = command;
                processCommand(command);
            };

            commandRecognition.onend = function() {
                listening = false;
                updateMic(false);
                setupRecognition();
            };

            commandRecognition.start();
            setTimeout(() => {
                if (listening) {
                    speak("Não entendi, pode repetir?");
                    listening = false;
                    updateMic(false);
                    setupRecognition();
                }
            }, 7000);
        }

        function processCommand(command) {
            let response = "Não entendi, pode repetir?";

            console.log("Processando comando:", command);  // Adicionado para debugging

            if (command.includes("joão liga")) {
                response = "Ligando o dispositivo.";
                sendCommandToArduino("ON");
            } else if (command.includes("joão desliga")) {
                response = "Desligando o dispositivo.";
                sendCommandToArduino("OFF");
            } else if (command.includes("opa")) {
                response = "Saindo...";
                speak(response);
                return; // Encerra o loop
            } else {
                response = "Comando não reconhecido.";
            }

            speak(response);
        }

        function sendCommandToArduino(command) {
            fetch('/send_command', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ command: command })
            })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Erro:', error));
        }

        function speak(text) {
            responsiveVoice.speak(text, "Brazilian Portuguese Female", {rate: 1.1});
            console.log("Falando:", text);
        }

        function updateMic(listening) {
            mic.style.backgroundColor = listening ? "red" : "blue";
            if (listening) {
                mic.classList.add("pulsing");
            } else {
                mic.classList.remove("pulsing");
            }
        }
    </script>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background-color: #222; color: white; }
        h1 { color: #00ff99; }
        p { font-size: 18px; }
        #mic {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: blue;
            margin: 20px auto;
            transition: background-color 0.5s;
        }
        .pulsing {
            animation: pulse 1s infinite;
        }
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>
    <h1>Maria - Assistente Virtual</h1>
    <p>Diga "Maria" para ativar.</p>
    <div id="mic"></div>
    <p id="content"></p>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/send_command", methods=["POST"])
def send_command():
    data = request.json
    command = data.get("command")
    
    try:
        with serial.Serial('COM3', 9600, timeout=1) as arduino:
            if command == "ON":
                arduino.write(b'ON\n')  # Envia comando para ligar
                return {"status": "success", "message": "Dispositivo ligado."}
            elif command == "OFF":
                arduino.write(b'OFF\n')  # Envia comando para desligar
                return {"status": "success", "message": "Dispositivo desligado."}
            else:
                return {"status": "error", "message": "Comando desconhecido."}
    except serial.SerialException as e:
        return {"status": "error", "message": f"Erro ao acessar a porta: {str(e)}"}

if __name__ == "__main__":
    app.run(debug=True)
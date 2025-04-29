# Maria Chatbot (via Flask)

Este projeto é um simples chatbot criado com Python e Flask que responde a comandos específicos passados por URL. Ele simula uma assistente virtual chamada Maria, com respostas básicas a comandos como "nome", "idade", "tchau", etc.

## 🔧 Tecnologias Utilizadas

- Python 3
- Flask (framework web)

## 🚀 Como Executar


 **Instale as dependências:**

```bash
pip install flask
```

. **Execute o servidor:**

```bash
python assistente.py
```

4 **Faça requisições GET no navegador ou Postman:**

```bash
http://127.0.0.1:5000/process_command?command=maria
```

## 💬 Comandos disponíveis

| Comando na URL | Resposta da Maria                      |
|----------------|----------------------------------------|
| maria          | Olá! Como posso te ajudar?             |
| nome           | Meu nome é Maria!                      |
| idade          | Eu sou um chatbot e não tenho idade.   |
| tchau          | Tchau! Tenha um bom dia!               |
| qualquer outro | Desculpe, não entendi o que você quis dizer. |



Criado por [Guilherme Voltolin Capodeferro](https://github.com/gui221227) 🚀

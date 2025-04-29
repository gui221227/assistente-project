# Maria Chatbot (via Flask)

Este projeto é um simples chatbot criado com Python e Flask que responde a comandos específicos passados por URL. Ele simula uma assistente virtual chamada Maria, com respostas básicas a comandos como "nome", "idade", "tchau", etc.

## 🔧 Tecnologias Utilizadas

- Python 3
- Flask (framework web)

## 🚀 Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. **Instale as dependências:**

```bash
pip install flask
```

3. **Execute o servidor:**

```bash
python app.py
```

4. **Faça requisições GET no navegador ou Postman:**

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

## 📂 Estrutura do Projeto

```
.
├── app.py         # Código principal com o servidor Flask
├── README.md      # Descrição do projeto
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Criado por [Seu Nome](https://github.com/seu-usuario) 🚀

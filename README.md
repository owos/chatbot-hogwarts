<h1 align="center">Chatbot Hogwarts :speech_balloon:</h1>
<p align="center">
<img src = https://img.shields.io/badge/RASA-Chatbot-blueviolet>
<img src = https://img.shields.io/badge/NLP-Machine%20learning-blue>
<img src = https://img.shields.io/badge/Python-Linguagem%20-brightgreen>
</p>

## Informações
- Autor : João Paulo Wakugawa 
- API : <a href="http://hp-api.herokuapp.com/">Harry-Potter</a>
- Link do Okteto : <a href="https://web-jpwakugawa.cloud.okteto.net/">Chat de Hogwarts</a>

---

## Funcionalidades
- [x] Fornecer tour pela escola
- [x] Contar curiosidades sobre Hogwarts
- [ ] Pesquisar personagem específico

---

## Projeto Local 
### Rasa
- Siga `bot`:
    ```bash
    rasa train
    rasa run --enable-api --cors "*"
    ```

### Rasa SDK
- Siga `bot` > `actions`:<br>
Adicione um arquivo **secrets.py** com as informações do seu cluster.
    ```python3
    secrets = {
        "CLUSTER": "your_cluster",
        "DB_NAME": "your_database",
        "COL_NAME": "your_collection"
    }
    ```

- Siga `bot`:
    ```bash
    rasa run actions
    ```

### Webchat
- Siga `web`:
    ```bash
    npm i
    npm run devStart
    ```

---

## Okteto
- Comando para deploy:
    ```bash
    okteto stack deploy --build
    ```

---

## Tecnologias e depêndencias :books:
- <a href="https://rasa.com/docs/rasa/installation/">Rasa</a>
- <a href="https://docs.python.org/3/">Python</a>
- <a href="https://docs.mongodb.com/">MongoDB</a>
- <a href="https://pymongo.readthedocs.io/en/stable/index.html">Pymongo</a>
- <a href="https://docs.docker.com/">Docker</a>
- <a href="https://okteto.com/docs/getting-started/index.html">Okteto</a>

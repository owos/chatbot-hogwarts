# Chatbot Hogwarts :speech_balloon:
## Informações
- Autor : João Paulo Wakugawa 
- API : <a href="http://hp-api.herokuapp.com/">Harry-Potter</a>
- Link do Okteto : <a href="https://web-jpwakugawa.cloud.okteto.net/">Chat de Hogwarts</a>

---

## Funcionalidades
- [x] Fornecer tour pela escola
- [ ] Contar fatos divertidos
- [ ] Pesquisar um personagem específico

---

## Utilizando o Rasa
- Siga `bot`:
    ```bash
    rasa init            # Criando uma pasta com config iniciais
    rasa train           # Treinando o modelo
    --fixed-model-name   # Flag para gerar modelo com nome específico
    rasa run actions     # Lembrar de reiniciar sempre que houver alterações
    rasa shell           # Testando as funcionalidades do modelo
    -vv                  # Flag para mostrar mais detalhes
    rasa interactive     # Auxilia na definição de uma story 
    ```

---

## Utilizando o Webchat
- Siga `web`:
    ```bash
    npm i
    npm run devStart
    ```

---

## Utilizando o Okteto
- Comando para deployar:
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

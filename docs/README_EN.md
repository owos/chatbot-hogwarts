## Local Environment

### Rasa Bot
- Go to `bot`:
    ```shell
    rasa train
    rasa run --enable-api --cors "*"
    ```

### Rasa SDK
- Go to `bot` > `actions`:<br>
Add a **secrets.py** file with your cluster information.
    ```python3
    secrets = {
        "CLUSTER": "your_cluster",
        "DB_NAME": "your_database",
        "COL_NAME": "your_collection"
    }
    ```

- Go to `bot`:
    ```shell
    rasa run actions
    ```

### Website
- Go to `web`:
    ```shell
    npm i
    npm run devStart
    ```

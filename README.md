# Gensim Model

This is an API service for `ModelGensim` of `coeus`

## API Documentation

### `GET /heathcheck`

Request: `None`

Response: `'OK'` with HTTP Status `200`

### `POST /predict/wmd`

Request:
`"data"` is an object contains `"word1"` and `"word2"` that want to get word mover distance between them.

```json
{
  "data": {
    "word1": "text",
    "word2": "text"
  }
}
```

Response:
`"result"` is a number represents word mover distance between `"word1"` and `"word2"`.

```json
{
  "result": 0.0
}
```

### `POST /predict/similarity`

Request:
`"data"` is an object contains `"word1"` and `"word2"` that want to get similarity score between them.

```json
{
  "data": {
    "word1": "text",
    "word2": "text"
  }
}
```

Response:
`"result"` is a number represents word mover distance between `"word1"` and `"word2"`.

```json
{
  "result": 1.0
}
```

### `POST /predict/word_embedding`

Request:
`"data"` is a text.

```json
{
  "data": "text"
}
```

Response:
`"result"` is an array represents word vectors.

```json
{
  "result": [
    0.279296875,
    -0.08447265625,
    -0.04150390625,
    0.1201171875,
    -0.0179443359375,
    0.12353515625,
    0.1328125,
    -0.08251953125,
    .
    .
    .
  ]
}
```

## Run

1. Copy file `.env.example` into `.env` and fill in all necessary values
2. Make sure you have Docker installed on your system and running
3. Build Docker image with a name of your choice if you haven't

```shell
docker build --tag gensim-api .
```

5. Spin up a server

```shell
docker run -d -p 5000:5000 --name gensim-api gensim-api
```

6. Try accessing [http://127.0.0.1:5000](http://127.0.0.1:5000) with a valid route
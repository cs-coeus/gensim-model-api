import os
from dotenv import dotenv_values
from flask import Flask, jsonify, request

from models.model import ModelGensim

is_production = os.environ.get('FLASK_ENV') == 'production'
authentication_token = os.environ.get('AUTHORIZATION_KEY')
config = dotenv_values(".env")

model = ModelGensim()
app = Flask(__name__)


@app.route('/healthcheck')
def health_check():
    return 'OK'


@app.route('/predict/wmd', methods=['POST'])
def predict_wmd():
    if request.method == 'POST' and request.json is not None:
        if is_production:
            token = request.headers.get('Authorization').split(' ')[1]
            if token != authentication_token:
                return jsonify({"error": "Unauthorized request"}), 403
        data = request.json['data']
        if data is not None:
            try:
                result = model.get_wmd(data['word1'], data['word2'])
                return jsonify({"result": result})
            except Exception as e:
                print(data, flush=True)
                print(e, flush=True)
                return jsonify({"error": "Data format wrong"}), 400
    return jsonify({"error": "Data is invalid or not exist"}), 400


@app.route('/predict/similarity', methods=['POST'])
def predict_similarity():
    if request.method == 'POST' and request.json is not None:
        if is_production:
            token = request.headers.get('Authorization').split(' ')[1]
            if token != authentication_token:
                return jsonify({"error": "Unauthorized request"}), 403
        data = request.json['data']
        if data is not None:
            try:
                result = model.get_similarity_two_word_by_w2v(data['word1'], data['word2'])
                return jsonify({"result": float(result)})
            except Exception as e:
                print(data, flush=True)
                print(e, flush=True)
                return jsonify({"error": "Data format wrong"}), 400
    return jsonify({"error": "Data is invalid or not exist"}), 400


@app.route('/predict/word_embedding', methods=['POST'])
def predict_word_embedding():
    if request.method == 'POST' and request.json is not None:
        if is_production:
            try:
                token = request.headers.get('Authorization').split(' ')[1]
            except Exception:
                return jsonify({"error": "Unauthorized"}), 403
            if token != authentication_token:
                return jsonify({"error": "Unauthorized request"}), 403
        data = request.json['data']
        if data is not None:
            try:
                result = model.get_word_embedding(data)
                return jsonify({"result": result})
            except Exception as e:
                print(data, flush=True)
                print(e, flush=True)
                return jsonify({"error": f"Data format wrong or unknown error occur, {e}"}), 500
    return jsonify({"error": "Data is invalid or not exist"}), 400

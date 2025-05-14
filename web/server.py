#!/usr/bin/env python3
from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Habilitar CORS para todas as rotas

@app.route('/')
def serve_index():
    """Serve o arquivo index.html na rota raiz."""
    return send_file('index.html')

@app.route('/app.js')
def serve_app_js():
    """Serve o arquivo app.js."""
    return send_from_directory('.', 'app.js')

@app.route('/login', methods=['POST'])
def login():
    """Lida com requisições POST para login."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Simula verificação (apenas para teste)
    if username and password:
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
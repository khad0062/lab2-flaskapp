# app.py
from flask import Flask, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename="login_attempts.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Example hardcoded credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    ip = request.remote_addr

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        logging.info(f"SUCCESSFUL LOGIN: user={username} ip={ip}")
        return jsonify({"message": "Login successful!"}), 200
    else:
        logging.warning(f"FAILED LOGIN: user={username} ip={ip}")
        return jsonify({"message": "Login failed!"}), 401

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

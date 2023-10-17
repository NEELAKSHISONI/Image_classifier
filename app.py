import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, request, jsonify, Response
from certificate_utils import sign_csr

from flask_sqlalchemy import SQLAlchemy
from user_management.models import db
from user_management.routes import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_management/db.sqlite'
db.init_app(app)
app.register_blueprint(user_bp, url_prefix='/user')


app = Flask(__name__)
SECRET_KEY = "9414686936@Papa"

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/csr', methods=['POST'])
def handle_csr():
    csr_data = request.data.decode('utf-8')
    signed_cert = sign_csr(csr_data, 'certs/ca_cert.pem', 'certs/ca_key.pem')
    return jsonify({"signed_certificate": signed_cert})

@app.route('/sign-csr', methods=['POST'])
def sign_certificate_request():
    csr_data = request.data
    signed_cert = sign_csr(csr_data, 'certs/ca_cert.pem', 'certs/ca_key.pem')
    return Response(signed_cert, mimetype='application/x-pem-file')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    users = {
        "username1": "password1",
        "username2": "password2"
    }

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        token = jwt.encode({
            'user': username,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, SECRET_KEY, algorithm="HS256")

        return jsonify({'token': token})

    return jsonify({'message': 'Invalid username or password'}), 401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/protected', methods=['GET'])
@token_required
def protected_route():
    return jsonify({'message': 'This is a protected route!'})

if __name__ == '__main__':
    context = ('certs/service_cert.pem', 'certs/service_key.pem', 'certs/ca_cert.pem')
    app.run(ssl_context=context, port=5000)

from flask import Blueprint, request, jsonify
import jwt
from models import Employee
from database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    emp = Employee.query.filter_by(email=email, password=password).first()
    if not emp:
        return jsonify({'error': 'Invalid credentials'}), 401
    token = jwt.encode({'id': emp.id}, 'supersecretkey', algorithm='HS256')
    return jsonify({'token': token})
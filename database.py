from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# -----------------------------
# routes/payroll.py
from flask import Blueprint, jsonify, request
from models import Employee
from auth import jwt

payroll_bp = Blueprint('payroll', __name__)

@payroll_bp.route('/api/payroll/<int:emp_id>', methods=['GET'])
def get_payroll(emp_id):
    emp = Employee.query.get(emp_id)
    if not emp:
        return jsonify({'error': 'Employee not found'}), 404
    tax_amount = emp.salary * emp.tax_percent / 100
    net_salary = emp.salary - tax_amount
    return jsonify({
        'name': emp.name,
        'base_salary': emp.salary,
        'tax_percent': emp.tax_percent,
        'net_salary': net_salary
    })
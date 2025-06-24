from flask import Blueprint, jsonify

workday_bp = Blueprint('workday', __name__)

@workday_bp.route('/api/workday/employee/<int:emp_id>', methods=['GET'])
def mock_workday_employee(emp_id):
    # Simulated response like Workday API
    return jsonify({
        'employeeId': emp_id,
        'firstName': 'Anuj',
        'lastName': 'Gadekar',
        'position': 'Software Engineer',
        'department': 'Engineering'
    })

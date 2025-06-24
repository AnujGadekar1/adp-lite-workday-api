from flask import Blueprint, request, jsonify
from models import LeaveRequest
from database import db

leave_bp = Blueprint('leave', __name__)

@leave_bp.route('/api/leave', methods=['POST'])
def submit_leave():
    data = request.json
    leave = LeaveRequest(**data)
    db.session.add(leave)
    db.session.commit()
    return jsonify({'message': 'Leave request submitted'})

@leave_bp.route('/api/leave/<int:emp_id>', methods=['GET'])
def get_leave(emp_id):
    leaves = LeaveRequest.query.filter_by(employee_id=emp_id).all()
    return jsonify([{
        'leave_type': l.leave_type,
        'start_date': l.start_date,
        'end_date': l.end_date
    } for l in leaves])
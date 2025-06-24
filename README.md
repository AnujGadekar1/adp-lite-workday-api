# ADP Lite - HR Payroll + Workday API Integration

A Flask-based project that simulates an ADP-like payroll system along with a mock Workday API integration.

## Features:
- Employee login (JWT-based auth)
- Payroll calculation (net salary)
- Leave request submission & tracking
- Mock Workday API response for employee info

## Run Locally
```bash
pip install -r requirements.txt
python app.py
```

## Sample API Call
```http
GET /api/workday/employee/1

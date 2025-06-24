 

 
# ADP Lite – Employee Payroll & Workday API Integration 🚀

A secure, lightweight Human Resource Management System built with **Flask**, simulating core features of **ADP** and **Workday**. This project showcases key enterprise HR functions such as employee payroll calculation, leave tracking, and external API-style data retrieval.

---

## ✨ Features

- 🔐 **JWT-based Authentication**  
  Secure login flow for employees using email/password.

- 💵 **Payroll Calculation API**  
  Returns gross salary, tax percentage, and net salary breakdown for employees.

- 📄 **Leave Management System**  
  Submit and fetch leave records by employee.

- 🌐 **Mock Workday API**  
  Simulates an external employee info system using a REST-style endpoint.

- 🧱 **Modular Flask Architecture**  
  Easy to scale, integrate, or extend with new microservices.

---

## 📦 Tech Stack

- **Backend**: Python, Flask  
- **Database**: SQLite (via SQLAlchemy ORM)  
- **Auth**: JWT  
- **API Format**: REST  
- **Tools**: Postman, VS Code

---

## 📁 Project Structure

```

adp-lite-workday-api/
├── app.py                 # Main application entry
├── auth.py                # JWT login logic
├── database.py            # DB connection & initialization
├── models.py              # SQLAlchemy ORM models
├── routes/
│   ├── payroll.py         # Payroll endpoint logic
│   ├── leave.py           # Leave request endpoints
│   └── workday\_api.py     # Mock Workday-style employee API
├── requirements.txt
└── README.md

````

---

## 🔧 Getting Started

### 1. Clone the repo
```bash
git clone  
cd adp-lite-workday-api
````

### 2. Set up virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

---

## 🧪 API Testing

Use **Postman** or **curl** to test these endpoints:

### 🔐 Login

```http
POST /login
{
  "email": 
  "password":  

### 💰 Get Payroll Info

```http
GET /api/payroll/1
Authorization: Bearer <your_token>
```

### 📄 Submit Leave

```http
POST /api/leave
{
  "employee_id": 1,
  "leave_type": "Casual",
  "start_date": "2025-06-25",
  "end_date": "2025-06-26"
}
```

### 📜 Workday API (Mock)

```http
GET /api/workday/employee/1
```

---

## 📌 About

This project was created by [Anuj Gadekar](https://github.com/AnujGadekar1) to demonstrate REST API design, authentication flow, and enterprise system simulation 

---

## 📄 License

MIT License

```

 

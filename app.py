from flask import Flask
from database import db, initialize_db
from auth import auth_bp
from routes.payroll import payroll_bp
from routes.leave import leave_bp
from routes.workday_api import workday_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adp.db'
app.config['SECRET_KEY'] = 'supersecretkey'

initialize_db(app)

app.register_blueprint(auth_bp)
app.register_blueprint(payroll_bp)
app.register_blueprint(leave_bp)
app.register_blueprint(workday_bp)

if __name__ == '__main__':
    app.run(debug=True)

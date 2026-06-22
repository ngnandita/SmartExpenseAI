from flask import Flask
from database.db import create_tables
from routes.auth import auth_bp
from routes.expense_routes import expense_bp

app = Flask(__name__)

create_tables()
app.register_blueprint(expense_bp)

app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return "SmartExpenseAI Backend Running"

if __name__ == "__main__":
    app.run(debug=True)
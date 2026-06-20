from flask import Flask
from database.db import create_tables

app = Flask(__name__)

create_tables()

@app.route("/")
def home():
    return "SmartExpenseAI Backend Running"

if __name__ == "__main__":
    app.run(debug=True)
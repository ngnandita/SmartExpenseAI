from flask import Blueprint, request, jsonify
from database.db import get_db_connection

expense_bp = Blueprint('expense', __name__)

# Add Expense
@expense_bp.route('/expenses', methods=['GET'])
def get_expenses():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    conn.close()

    return jsonify([dict(expense) for expense in expenses])

    data = request.get_json()

    user_id = data['user_id']
    amount = data['amount']
    category = data['category']
    description = data['description']
    date = data['date']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses
        (user_id, amount, category, description, date)
        VALUES (?, ?, ?, ?, ?)
        """,
        (user_id, amount, category, description, date)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Expense Added Successfully"
    })
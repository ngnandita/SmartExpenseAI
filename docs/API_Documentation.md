# SmartExpenseAI API Documentation

## Base URL

http://127.0.0.1:5000

---

# 1. User Registration

## Endpoint

POST /register

## Request Body

```json
{
  "name": "Nandita",
  "email": "nandita@gmail.com",
  "password": "123456"
}
```

## Success Response

```json
{
  "message": "User Registered Successfully"
}
```

## Status Code

201 Created

---

# 2. User Login

## Endpoint

POST /login

## Request Body

```json
{
  "email": "nandita@gmail.com",
  "password": "123456"
}
```

## Success Response

```json
{
  "message": "Login Successful",
  "user": {
    "id": 1,
    "name": "Nandita",
    "email": "nandita@gmail.com"
  }
}
```

## Error Response

```json
{
  "message": "Invalid Email or Password"
}
```

## Status Code

200 OK

401 Unauthorized

---

# Future APIs (Week 2)

## Add Expense

POST /expenses

### Request

```json
{
  "amount": 500,
  "category": "Food",
  "description": "Pizza",
  "date": "2026-06-22"
}
```

---

## Get Expenses

GET /expenses

---

## Update Expense

PUT /expenses/{id}

---

## Delete Expense

DELETE /expenses/{id}
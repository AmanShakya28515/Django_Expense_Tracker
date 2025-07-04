# Django Expense Tracker API

## Project Overview

This project implements a RESTful API for managing personal expense and income records with secure user authentication. Users can create, view, update, and delete their own expense/income data, while superusers have access to all users' records. The API also includes automatic tax calculation (flat or percentage) and supports paginated responses.

## Features

- User registration and JWT-based authentication (login, token refresh)

- Role-based access control:
  - Regular users manage only their own records
  - Superusers have full access to all records

- CRUD operations on expense/income records

- Automatic tax calculation with flat or percentage options

- Paginated list endpoints for scalable data retrieval

- Secure endpoints with permission checks

- Clear API response formats for single and list records

# Technologies Used

- Python 3.8+

- Django

- Django REST Framework

- djangorestframework-simplejwt (JWT Authentication)

- SQLite (development database)
  
- Postman (for API testing)

## Setup Instructions

- Python 3.8 or higher installed

- Git installed

- Virtual environment tool 

### Installation Steps

1. Clone the repository

2. Create and activate a virtual environment

3. Install dependencies
   pip install -r requirements.txt

4. Apply migrations

5. Run the development server

=====================

## API Endpoints

### Authentication

**POST** `/auth/register/`

  Register a new user.
  Allows a new user to register using a unique username and password.
  (JSON)
  {
  "username": "your_username",
  "password": "your_password"
  }
  Successful Response (201 Created): <==shows if Created

- **POST** `/auth/login/`  
  Obtain JWT access and refresh tokens.
  Logs in a user and returns a pair of JSON Web Tokens (access and refresh) for authentication.
  (JSON)
  {
  "username": "your_username",
  "password": "your_password"
  }

  Successful Response (200 OK): <==== shows if logged in 
  and provides ...
  {
  "refresh": "your_refresh_token",
  "access": "your_access_token"
  }

- **POST** `/auth/refresh/`  
  Refresh access token.
  Gets a new access token using a valid refresh token (no need to log in again).
  (JSON)
  {
  "refresh": "your_refresh_token"
  }
  shows Successful Response (200 OK) if success


### Expense Management

- **GET** `/expenses/`  
  List authenticated user's records (paginated).

- **POST** `/expenses/`  
  Create a new expense/income record.

- **GET** `/expenses/{id}/`  
  Retrieve a specific record by ID.

- **PUT** `/expenses/{id}/`  
  Update a specific record by ID.

- **DELETE** `/expenses/{id}/`  
  Delete a specific record by ID.

  ## Example Usage

### Register User

POST /auth/register/
Content-Type: application/json

{
  "username": "userone",
  "password": "oenpass3"
}

### Login
POST /auth/login/
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass123"
}

# Response
{
  "refresh": "refresh_token",
  "access": "access_token"
}

### Crud 
# CreateExpense
POST /expenses/

{
  "title": "Grocery Shopping",
  "amount": 100,
  "description": "Weekly groceries",
  "transaction_type": "debit",
  "tax": 10,
  "tax_type": "flat"
}

# list expenses  ====> Paginated API responses , these are the data from the database 
GET /expenses/?page=1'

{
  "count": 6,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 2,
      "title": "Grocery",
      "amount": "100.00",
      "transaction_type": "credit",
      "total": 110.0,
      "created_at": "2025-07-04T13:41:33.149578Z"
    },
    {
      "id": 3,
      "title": "Grocery",
      "amount": "100.00",
      "transaction_type": "credit",
      "total": 110.0,
      "created_at": "2025-07-04T13:41:37.569650Z"
    },
    {
      "id": 4,
      "title": "ClothShopping",
      "amount": "900.00",
      "transaction_type": "debit",
      "total": 905.0,
      "created_at": "2025-07-04T14:28:05.138293Z"
    },
    {
      "id": 5,
      "title": "ShoesShopping",
      "amount": "1000.00",
      "transaction_type": "debit",
      "total": 1005.0,
      "created_at": "2025-07-04T14:38:11.640998Z"
    },
    {
      "id": 6,
      "title": "BooksBuy",
      "amount": "100.00",
      "transaction_type": "debit",
      "total": 105.0,
      "created_at": "2025-07-04T14:38:49.364698Z"
    }
  ]
}

# UpdateExpense
PUT /expenses/1/

{
  "title": "Grocery Shopping Updated",
  "amount": 120,
  "description": "Weekly groceries and snacks",
  "transaction_type": "debit",
  "tax": 12,
  "tax_type": "flat"
}

# DeletExpense

DELETE /expenses/1/

## In conclusion i have added the expected API Response Format and paginated data which have been added in upper code in list expenses

{
  "id": 4,
  "title": "ClothShopping",
  "description": "I am travelling around with my friends to buy clothings",
  "amount": "900.00",
  "transaction_type": "debit",
  "tax": "5.00",
  "tax_type": "flat",
  "created_at": "2025-07-04T14:28:05.138293Z",
  "updated_at": "2025-07-04T14:28:05.138266Z",
  "total": 905.0
}

============================
This API is built with secure practices and provides clear structure for managing expenses effectively. The paginated responses, JWT security, and tax features make it production-ready.
## Thankyou 




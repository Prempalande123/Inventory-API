# 🧾 Inventory Management API

A RESTful API built using **Django** and **Django REST Framework (DRF)** to manage inventory items, categories, and stock levels. Includes secure JWT authentication for user access control.

---

## 🚀 Features

- 📦 CRUD operations for inventory items
- 🏷️ Category management
- 🔐 JWT Authentication (Simple JWT)
- 🔍 Search, Filter, Order, and Pagination support
- 🛡️ Role-based access (Admin vs Regular Users)

---

## ⚙️ Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- Simple JWT for token-based auth
- SQLite (default)

---

## 🔐 Authentication

### 1. Obtain Token

POST `/api/token/`

```json
{
  "username": "your_username",
  "password": "your_password"
}

### 2.  Documented APIs using Swagger UI and ReDoc for interactive and comprehensive API reference

1) http://127.0.0.1:8000/swagger/
2) http://127.0.0.1:8000/redoc/

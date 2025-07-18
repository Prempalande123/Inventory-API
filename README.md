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

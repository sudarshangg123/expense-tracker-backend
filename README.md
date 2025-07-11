# 💰 Expense Tracker Backend (Django + DRF)

A simple backend system that allows authenticated users to track their daily expenses, view filtered lists, and get powerful analytics including category breakdown and spending trends.

---

## 🚀 Features

- ✅ JWT-based user authentication
- ✅ Add new expenses
- ✅ Filter expenses by date range
- ✅ Analytics:
  - Total expenses in a period
  - Category-wise breakdown
  - Daily / Weekly / Monthly expense trends

---

## ⚙️ Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework (DRF)
- SimpleJWT (JWT Authentication)
- SQLite (Relational DB)

---

## 🔐 Authentication

### Login
**Endpoint:** `/api/login/`  
**Method:** `POST`  
**Request:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**
```json
{
  "access": "your_jwt_access_token",
  "refresh": "your_jwt_refresh_token"
}
```

Use the access token in all other requests:
```
Authorization: Bearer <access_token>
```

---

## 📬 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/login/` | Login and get access + refresh token |
| POST | `/api/expenses/` | Create a new expense |
| GET | `/api/expenses/list/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` | List expenses filtered by date |
| GET | `/api/expenses/analytics/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` | View expense analytics |

---

## 📊 Analytics Output Sample

```json
{
  "total_expenses": 4450.0,
  "category_breakdown": [
    {"category": "FOOD", "total": 550.0},
    {"category": "RENT", "total": 1200.0}
  ],
  "daily_trend": [
    {"day": "2025-07-10", "total": 250.0, "average": 250.0}
  ],
  "weekly_trend": [
    {"week": "2025-07-08", "total": 1450.0, "average": 725.0}
  ],
  "monthly_trend": [
    {"month": "2025-07-01", "total": 4450.0, "average": 635.71}
  ]
}
```

---

## 🛠️ Setup Instructions (Local)

```bash
git clone https://github.com/sudarshangg123/expense-tracker-backend.git
cd expense-tracker-backend

python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🧪 Test with Postman

1. Login → `/api/login/` → Get token
2. Add expenses → `/api/expenses/`
3. List expenses → `/api/expenses/list/?start_date=...`
4. View analytics → `/api/expenses/analytics/?start_date=...`

---

## 📸 Screenshots

Place your Postman screenshots inside the `screenshots/` folder:

- `1_login_token.png`
- `2_create_expense.png`
- `3_list_expenses.png`
- `4_analytics_output.png`

---

## 🙋 About the Developer

**👨‍💻 Sudarshan Gujuri**  
Email: sudarshang8018@gmail.com
Phone_no - 9337955920
Date: 2025-07-11

---

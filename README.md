# 🚀 MAD2 Project Demo App

This is a full-stack demo application with:

* Backend (Python)
* Frontend (Node.js)
* Celery for background tasks
* Redis (message broker)
* Mail service (MailHog or Gmail SMTP)

---

## 📦 Prerequisites

Make sure you have the following installed:

* Python (3.8+)
* Node.js (16+ recommended)
* Redis
* MailHog (optional for local email testing)

### 🔗 Setup Resources

Refer to this guide for installing Redis and MailHog (Windows/Linux/macOS):
https://drive.google.com/drive/folders/123Uo5VzTIVHPWp7RyAyOyCgSPD-FlZaX

---

## ⚙️ Backend Setup

```bash
cd backend
```

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 To update dependencies:

```bash
pip freeze > requirements.txt
```

### 4. Run Backend Server

```bash
python app.py
```

---

## 🌐 Frontend Setup

```bash
cd frontend
```

### 1. Install Dependencies

```bash
npm install
```

### 2. Run Development Server

```bash
npm run dev
```

---

## 🔁 Celery Setup (Background Workers)

Make sure Redis is running before starting Celery.

### ▶️ Start Worker

Activate backend virtual environment first.

* **Windows:**

```bash
celery -A celery_app.app worker --pool=solo --loglevel=info
```

* **Linux / macOS:**

```bash
celery -A celery_app.app worker --loglevel=info
```

---

### ⏰ Start Celery Beat (Scheduler)

```bash
celery -A celery_app.app beat --loglevel=info
```

---

## 📧 Email Configuration

You can use either:

### Option 1: MailHog (Recommended for Development)

* Runs locally
* SMTP: `localhost:1025`
* Web UI: http://localhost:8025

---

### Option 2: Gmail SMTP

Update your backend config:

```python
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_app_password'
```

> ⚠️ Use **App Password**, not your Gmail password.

---

## 🧠 Notes

* Replace `localhost` URLs in emails with a real domain for production.
* Ensure Redis is running before Celery.
* Keep secrets (like email passwords) in environment variables.

---

## 🛠️ Tech Stack

* Backend: Python (Flask/FastAPI)
* Frontend: Node.js (Vite/React)
* Task Queue: Celery
* Broker: Redis
* Email: SMTP (MailHog / Gmail)

---

## ✅ You're Ready!

Start all services:

1. Redis
2. Backend server
3. Frontend server 
4. Celery worker
5. Celery beat

And you're good to go 🚀

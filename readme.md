# 📡 GitHub Webhook Listener with Flask + MongoDB

This project listens to GitHub webhook events (`push`, `pull_request`, and `merge`) via GitHub Actions and stores them in MongoDB. It provides an API to fetch and display these events in a human-readable format — perfect for building dashboards that poll every 15 seconds.

---

## 🚀 Features

- ✅ Listens to GitHub events (Push, Pull Request, Merge)
- ✅ Stores data in MongoDB
- ✅ Flask-based REST API to fetch recent activity
- ✅ Frontend-ready format
- ✅ Deployable to [Railway](https://railway.app/), [Render](https://render.com/), or any server

---

## 📂 Project Structure

```
├── app/
│ └── init.py # Flask app & routes
├── run.py # App entrypoint
├── Procfile # For Railway deployment
├── requirements.txt
├── .env # Environment variables
└── README.md
```
##  Create virtual environment & install dependencies
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

```
## configure env
```
FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/github_events

```
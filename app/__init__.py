from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Connect to MongoDB
    mongoUri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(mongoUri)
    db = client.github_events  # <-- your DB

    @app.route('/')
    def index():
        return "Webhook listener is running."

    @app.route('/webhook', methods=['POST'])
    def receive_event():
        data = request.get_json()
        data['receivedAt'] = datetime.utcnow()
        db.events.insert_one(data)  # ✅ Working insert
        return jsonify({"status": "received"}), 200

    @app.route('/events', methods=['GET'])
    def get_events():
        cursor = db.events.find().sort("receivedAt", -1).limit(20)
        events = []
        for doc in cursor:
            e = format_event(doc)
            if e:
                events.append(e)
        return jsonify(events)

    def format_event(event):
        timestamp = event.get("timestamp")
        time_str = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %B %Y - %I:%M %p UTC")
        author = event.get("sender")
        ref = event.get("ref", "")
        from_branch = event.get("head_ref")
        to_branch = event.get("base_ref") or ref.split("/")[-1]

        if event["event"] == "push":
            return f'"{author}" pushed to "{to_branch}" on {time_str}'
        elif event["event"] == "pull_request":
            if event.get("action") == "closed" and event.get("pull_request", {}).get("merged", False):
                return f'"{author}" merged branch "{from_branch}" to "{to_branch}" on {time_str}'
            else:
                return f'"{author}" submitted a pull request from "{from_branch}" to "{to_branch}" on {time_str}'
        return None

    return app

import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"name": "Complete Docker Task 4", "priority": "High", "status": "In Progress"},
    {"name": "Test container deployment", "priority": "Medium", "status": "Pending"}
]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    name = request.form.get("name")
    priority = request.form.get("priority")

    if name:
        tasks.append({
            "name": name,
            "priority": priority,
            "status": "Pending"
        })

    return redirect(url_for("home"))

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "IsaraTaskManagerDocker",
        "environment": os.getenv("APP_ENV", "development")
    }, 200

if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 5000))
    app.run(host="0.0.0.0", port=port)
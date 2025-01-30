from flask import Flask, request, jsonify
from datetime import datetime, timezone
from flask_cors import CORS
import pytz

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "email": "apatirasummie@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Summiedev/HNG_BACKEND_TASK"
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
import pytz

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "email": "apatirasummie@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/Summiedev"
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
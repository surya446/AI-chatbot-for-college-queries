from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or 5000 locally
    app.run(debug=True, host="0.0.0.0", port=port)

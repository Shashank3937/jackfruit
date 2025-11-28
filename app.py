from flask import Flask, render_template, request, jsonify
from bot import ChatBot

app = Flask(__name__)
# Create chatbot instance (mode can be 'rule' or 'openai')
# For local use choose mode='rule'. To use OpenAI set mode='openai' and export OPENAI_API_KEY.
bot = ChatBot(mode='rule')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/get", methods=["POST"])
def api_get():
    data = request.get_json() or {}
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400
    response = bot.get_response(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    # For development only. In production use a proper WSGI server.
    app.run(debug=True, host="127.0.0.1", port=5000)

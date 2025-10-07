from flask import Flask, request, jsonify
from kenbot import chat_with_bot  # keep your original KenBot logic

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    """
    Expects JSON: {"message": "your text here"}
    Returns JSON: {"reply": "KenBot's response"}
    """
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        if not user_message.strip():
            return jsonify({"reply": "You didn't type anything!"})

        bot_reply = chat_with_bot(user_message)
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Error in KenBot API: {e}")
        return jsonify({"reply": "KenBot is having trouble responding right now."})

if __name__ == "__main__":
    print("Starting local KenBot API on port 5001...")
    app.run(host="127.0.0.1", port=5001)

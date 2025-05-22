from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load Hugging Face chatbot model (example: conversational pipeline)
chatbot = pipeline("conversational")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    from transformers import Conversation
    conv = Conversation(user_input)
    result = chatbot(conv)
    reply = result.generated_responses[-1]

    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
     return "Flask Server is Running"

@app.route('/feedback', methods=['POST'])
def feedback():
     data = request.get_json(force=True)
     message = (data or {}).get('message', '').strip()
     if not message:
          return jsonify({"error": "No message provided"}), 400
     print(f"SERVER - Feedback received: {message}")
     return jsonify({"response": f"Thanks! You said: {message}"}), 201

if __name__ == '__main__':
     app.run(debug=True, port=5050)
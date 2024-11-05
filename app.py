# app.py
from flask import Flask
from flask_cors import CORS  
from apis import get_transcript_details

app = Flask(__name__)

# Allowed origins for frontend requests
CORS(app, origins=["http://localhost:3000"])  

@app.route('/', methods=['GET'])
def index():
    return "Server is up and running!"

app.add_url_rule('/earnings_transcript_summary', view_func=get_transcript_details, methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
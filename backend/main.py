from flask import Flask
from flask_cors import CORS
from api.test import api_bp

app = Flask(__name__)
CORS(app,origins=["http://localhost:3001/",'http://localhost:5173'])
app.register_blueprint(api_bp)

@app.route("/api/hello")
def hello():
    print("Hello from backend!")
    return "Hello from backend!"

@app.route("/")
def index():
    return "Welcome to the LeetSquad Backend! this is it"
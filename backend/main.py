from flask import Flask
from flask_cors import CORS
from api.test import api_bp
from api.auth import auth_bp
from supabase import create_client
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.config["SUPABASE_URL"] = os.getenv("SUPABASE_URL")
app.config["SUPABASE_KEY"] = os.getenv("SUPABASE_KEY")
supabase_client = create_client(app.config["SUPABASE_URL"], app.config["SUPABASE_KEY"])
app.dbclient = supabase_client


CORS(app,origins=["http://localhost:3001","http://localhost:5173"])
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)

@app.route("/api/hello")
def hello():
    response = supabase_client.table("TEST").insert({"id": 2,"name":"kudu"}).execute()
    response = supabase_client.auth.sign_up(
    {
        "email": "email@example.com",
        "password": "password",
    }
)

    print("Hello its",response)


    return "Hello from backend!"

@app.route("/")
def index():
    return "Welcome to the LeetSquad Backend! this is it"
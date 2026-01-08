from flask import Blueprint, current_app, request, jsonify
from supabase import Client

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/signup", methods=["POST"])
def signup():
    email, password = request.form.get("email").strip(), request.form.get("password").strip()
    leetcodeusername = request.form.get("leetcodeusername","").strip()
    print(email, password)

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    try:
        supabase: Client = current_app.dbclient
        response = supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
                "options": {"data": {"leetcodeusername": leetcodeusername}}
            }
        ) 
    except Exception as e:
        print("Error during sign up:", e)
        return jsonify({"error": str(e)}), 500


    return jsonify({"message": "User signed up successfully", "user": response["user"]}), 201


@auth_bp.route("/api/login", methods=["POST"])
def login():
    email, password = request.form.get("email").strip(), request.form.get("password").strip()
    print(email, password)

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    try:
        supabase: Client = current_app.dbclient
        response = supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password,
            }
        ) 
    except Exception as e:
        print("Error during login:", e)
        return jsonify({"error": str(e)}), 500


    return jsonify({"message": "User logged in successfully", "user": response["user"]}), 200
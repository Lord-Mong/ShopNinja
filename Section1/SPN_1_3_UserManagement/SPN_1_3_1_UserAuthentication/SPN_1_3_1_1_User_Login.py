# ===========================
# SPN_1_3_1_1_User_Login
# Section: Core Setup
# Component: User Management
# Module: Authentication
# Unit: User Login
# Purpose: Authenticate users during login and generate access tokens.
# Input: Username and password.
# Output: Authentication status, access token, or error message.
# ===========================

from flask import jsonify, request

def user_login(logger):
    """
    Authenticates users during login and generates an access token.

    Args:
        logger: Logger instance to log messages.

    Returns:
        Response: Flask JSON response indicating login success or failure.
    """
    try:
        data = request.get_json()

        # Extract user credentials
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            logger.error("Username or password missing.")
            return jsonify({"error": "Username and password are required."}), 400

        # Simulated authentication logic (replace with database or external validation)
        if username == "test_user" and password == "test_password":
            logger.info(f"User {username} successfully authenticated.")
            return jsonify({
                "message": "Login successful.",
                "token": "example_access_token"  # Replace with real token generation logic
            }), 200
        else:
            logger.warning(f"Invalid credentials for user {username}.")
            return jsonify({"error": "Invalid username or password."}), 401

    except Exception as e:
        logger.error(f"Error in user login: {e}")
        return jsonify({"error": "An unexpected error occurred during login."}), 500

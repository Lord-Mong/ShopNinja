# ===========================
# SPN_1_3_1_3_Token_Verification
# Section: Core Setup
# Component: User Management
# Module: Authentication
# Unit: Token Verification
# Purpose: Verify the validity of user tokens for authentication.
# Input: Access token.
# Output: Verification status (valid or invalid).
# ===========================

import jwt
from flask import jsonify, request

# Example secret key (replace with secure key management in production)
SECRET_KEY = "example_secret_key"

def verify_token(logger):
    """
    Verifies the validity of a user token.

    Args:
        logger: Logger instance to log messages.

    Returns:
        Response: Flask JSON response indicating token validity or error message.
    """
    try:
        # Retrieve token from headers
        token = request.headers.get("Authorization")
        if not token:
            logger.error("Missing authorization token.")
            return jsonify({"error": "Authorization token is required."}), 401

        try:
            # Decode and validate the token
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            logger.info(f"Token verified successfully for user: {payload.get('username')}")
            return jsonify({"message": "Token is valid.", "user": payload.get("username")}), 200

        except jwt.ExpiredSignatureError:
            logger.warning("Token has expired.")
            return jsonify({"error": "Token has expired."}), 401

        except jwt.InvalidTokenError:
            logger.warning("Invalid token.")
            return jsonify({"error": "Invalid token."}), 401

    except Exception as e:
        logger.error(f"Error during token verification: {e}")
        return jsonify({"error": "An unexpected error occurred during token verification."}), 500

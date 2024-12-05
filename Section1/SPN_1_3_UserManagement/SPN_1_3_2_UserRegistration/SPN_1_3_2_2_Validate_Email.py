# ===========================
# SPN_1_3_2_2_Validate_Email
# Section: Core Setup
# Component: User Management
# Module: User Registration
# Unit: Validate Email
# Purpose: Validate the format of user email addresses.
# Input: Email address string.
# Output: Validation result (valid or invalid).
# ===========================

import re
from flask import jsonify, request

def validate_email(logger):
    """
    Validates the format of an email address.

    Args:
        logger: Logger instance to log messages.

    Returns:
        Response: Flask JSON response indicating whether the email is valid or invalid.
    """
    try:
        data = request.get_json()

        # Extract email address
        email = data.get("email")
        if not email:
            logger.error("Email address is missing.")
            return jsonify({"error": "Email address is required."}), 400

        # Regular expression for validating email
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(email_regex, email):
            logger.info(f"Email address {email} is valid.")
            return jsonify({"message": "Email address is valid."}), 200
        else:
            logger.warning(f"Email address {email} is invalid.")
            return jsonify({"error": "Invalid email address."}), 400

    except Exception as e:
        logger.error(f"Error during email validation: {e}")
        return jsonify({"error": "An unexpected error occurred during email validation."}), 500

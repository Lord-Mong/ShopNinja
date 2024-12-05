# ===========================
# SPN_1_3_2_3_Duplicate_Check
# Section: Core Setup
# Component: User Management
# Module: User Registration
# Unit: Duplicate Check
# Purpose: Check for duplicate users based on username or email.
# Input: Username or email address.
# Output: Duplicate check result (exists or not).
# ===========================

from flask import jsonify, request

def check_duplicate(logger, db_session, UserModel):
    """
    Checks for duplicate users in the database based on username or email.

    Args:
        logger: Logger instance to log messages.
        db_session: Database session instance.
        UserModel: SQLAlchemy model class for the user.

    Returns:
        Response: Flask JSON response indicating whether the user exists.
    """
    try:
        data = request.get_json()

        # Extract username and email
        username = data.get("username")
        email = data.get("email")

        if not username and not email:
            logger.error("Both username and email are missing.")
            return jsonify({"error": "At least one of username or email is required."}), 400

        # Query the database for duplicates
        duplicate_user = None
        if username:
            duplicate_user = db_session.query(UserModel).filter_by(username=username).first()
            if duplicate_user:
                logger.warning(f"Duplicate username found: {username}")
                return jsonify({"error": "Username already exists."}), 409

        if email:
            duplicate_user = db_session.query(UserModel).filter_by(email=email).first()
            if duplicate_user:
                logger.warning(f"Duplicate email found: {email}")
                return jsonify({"error": "Email already exists."}), 409

        logger.info("No duplicates found.")
        return jsonify({"message": "No duplicates found."}), 200

    except Exception as e:
        logger.error(f"Error during duplicate check: {e}")
        return jsonify({"error": "An unexpected error occurred during duplicate check."}), 500

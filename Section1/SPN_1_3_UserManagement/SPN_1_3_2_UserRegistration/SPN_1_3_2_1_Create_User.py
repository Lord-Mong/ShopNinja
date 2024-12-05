# ===========================
# SPN_1_3_2_1_Create_User
# Section: Core Setup
# Component: User Management
# Module: User Registration
# Unit: Create User
# Purpose: Register new users and add them to the database.
# Input: User details (e.g., username, email, password).
# Output: Registration success or error message.
# ===========================

from flask import jsonify, request
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

def create_user(logger, db_session, UserModel):
    """
    Registers a new user and adds their details to the database.

    Args:
        logger: Logger instance to log messages.
        db_session: Database session instance.
        UserModel: SQLAlchemy model class for the user.

    Returns:
        Response: Flask JSON response indicating success or failure.
    """
    try:
        data = request.get_json()

        # Extract user details
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            logger.error("Username, email, or password is missing.")
            return jsonify({"error": "All fields (username, email, password) are required."}), 400

        # Hash the password for security
        hashed_password = generate_password_hash(password)

        # Create a new user instance
        new_user = UserModel(username=username, email=email, password=hashed_password)

        # Add user to the database
        db_session.add(new_user)
        db_session.commit()

        logger.info(f"User {username} registered successfully.")
        return jsonify({"message": "User registered successfully."}), 201

    except IntegrityError:
        logger.error(f"User with username or email already exists.")
        return jsonify({"error": "Username or email already exists."}), 409

    except Exception as e:
        logger.error(f"Error during user registration: {e}")
        return jsonify({"error": "An unexpected error occurred during registration."}), 500

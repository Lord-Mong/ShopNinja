# ===========================
# SPN_1_3_1_2_User_Logout
# Section: Core Setup
# Component: User Management
# Module: Authentication
# Unit: User Logout
# Purpose: Log out a user by clearing their session or token.
# Input: User session or token.
# Output: Logout status or error message.
# ===========================

from flask import jsonify, session

def user_logout(logger):
    """
    Logs out the user by clearing their session or invalidating their token.

    Args:
        logger: Logger instance to log messages.

    Returns:
        Response: Flask JSON response indicating logout success or failure.
    """
    try:
        # Clear session data (or token invalidation in a real implementation)
        session.clear()
        logger.info("User successfully logged out.")
        return jsonify({"message": "Logout successful."}), 200

    except Exception as e:
        logger.error(f"Error during logout: {e}")
        return jsonify({"error": "An unexpected error occurred during logout."}), 500

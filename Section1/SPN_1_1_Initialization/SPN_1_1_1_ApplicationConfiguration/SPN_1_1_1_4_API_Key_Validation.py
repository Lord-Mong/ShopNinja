# ===========================
# SPN_1_1_1_4_API_Key_Validation
# Section: Core Setup
# Component: Initialization
# Module: Application Configuration
# Unit: API Key Validation
# Purpose: Validate the format and presence of required API keys.
# Input: Environment variables containing API keys.
# Output: Validation status and error messages (if any).
# ===========================

import os

def validate_api_keys(logger, required_keys):
    """
    Validates the presence and format of required API keys.

    Args:
        logger: Logger instance to log messages.
        required_keys (list): List of required API keys.

    Returns:
        dict: Dictionary with validation status and error messages.
    """
    logger.info("Validating API keys...")

    validation_results = {}
    for key in required_keys:
        value = os.environ.get(key, None)
        if value is None:
            validation_results[key] = "Missing"
            logger.error(f"API key '{key}' is missing.")
        elif not value.strip():
            validation_results[key] = "Empty"
            logger.error(f"API key '{key}' is empty.")
        else:
            validation_results[key] = "Valid"
            logger.info(f"API key '{key}' is valid.")

    return validation_results

# ===========================
# SPN_1_1_1_2_API_Key_Environment_Setup
# Section: Core Setup
# Component: Initialization
# Module: Application Configuration
# Unit: API Key Environment Setup
# Purpose: Load API keys and environment variables for the application.
# Input: Logger instance to log messages.
# Output: Dictionary of loaded environment variables.
# ===========================

import os
from dotenv import load_dotenv, find_dotenv

# Logger will be passed as a parameter to avoid circular issues
def load_environment_variables(logger):
    """
    Loads environment variables for the application from a .env file.
    Args:
        logger: Logger instance to log messages.
    """
    try:
        env_file = find_dotenv()
        load_dotenv(env_file)
        logger.info(f"Environment variables successfully loaded from .env file: {env_file}")
    except Exception as e:
        logger.error(f"Failed to load environment variables from .env file: {e}")

    # Ensure required API keys are loaded
    required_keys = ["OPENAI_API_KEY"]
    missing_keys = []

    for key in required_keys:
        if not os.getenv(key):
            missing_keys.append(key)

    if missing_keys:
        logger.error(f"Missing required environment variables: {', '.join(missing_keys)}")
    else:
        logger.info("All required API keys successfully loaded.")

def load_api_keys(logger):
    """
    Loads API keys into the environment and removes placeholder values.
    Args:
        logger: Logger instance to log messages.
    """
    # Load placeholder API keys
    api_keys = {
        "API_KEY_1": os.getenv("API_KEY_1", "YOUR_API_KEY_1_HERE"),
        "API_KEY_2": os.getenv("API_KEY_2", "YOUR_API_KEY_2_HERE"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY_HERE")
    }

    # Remove any placeholder keys that are not set
    for key, value in api_keys.items():
        if value in ["YOUR_API_KEY_1_HERE", "YOUR_API_KEY_2_HERE", "YOUR_OPENAI_API_KEY_HERE"]:
            logger.warning(f"API key for {key} is not set. Please provide a valid value.")
            if key in os.environ:
                del os.environ[key]
        else:
            os.environ[key] = value
            logger.info(f"API key for {key} successfully loaded.")

    # Additional handling for missing API keys
    if "MISSING_API_KEY" in os.environ:
        del os.environ["MISSING_API_KEY"]
        logger.warning("Removed placeholder key: MISSING_API_KEY")
    
    # Debugging to show final environment state (for development purposes)
    logger.debug("Final environment variables loaded:")
    for key, value in os.environ.items():
        if "KEY" in key:
            logger.debug(f"{key}: {value}")

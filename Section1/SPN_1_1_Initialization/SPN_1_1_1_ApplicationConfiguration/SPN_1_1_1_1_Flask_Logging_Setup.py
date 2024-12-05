# ===========================
# SPN_1_1_1_1_Flask_Logging_Setup
# Section: Core Setup
# Component: Initialization
# Module: Application Configuration
# Unit: Flask Logging Setup
# Purpose: Set up logging and initialize the Flask application.
# Input: Logging level (default: INFO).
# Output: Configured Flask application instance and logger.
# ===========================

import logging
from flask import Flask

def initialize_flask_app(logging_level=logging.INFO):
    """
    Initializes the Flask application and configures logging.

    Args:
        logging_level (int): Logging level to configure. Defaults to INFO.

    Returns:
        Flask: Initialized Flask app instance.
        Logger: Configured logging instance.
    """
    # Configure Logging
    logging.basicConfig(
        level=logging_level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger("ShopNinjaLogger")
    logger.info("Logging initialized.")

    # Create Flask App
    app = Flask(__name__)
    logger.info("Flask application initialized.")

    return app, logger

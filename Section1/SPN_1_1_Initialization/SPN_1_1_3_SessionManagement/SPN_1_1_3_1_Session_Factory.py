# ===========================
# SPN_1_1_3_1_Session_Factory
# Section: Core Setup
# Component: Initialization
# Module: Session Management
# Unit: Session Factory
# Purpose: Configures session and database management for the application.
# Input: Flask application instance and logger.
# Output: Configured Flask application with session management enabled.
# ===========================

from flask_caching import Cache

def initialize_session_management(app, logger):
    """
    Configures session management for the Flask application using CacheLib.

    Args:
        app: Flask application instance to configure session management for.
        logger: Logger instance to log messages.

    Returns:
        None
    """
    logger.info("Initializing session management...")

    try:
        # Configure session storage using filesystem
        app.config["SESSION_TYPE"] = "filesystem"
        app.config["SESSION_FILE_DIR"] = "./flask_session"
        app.config["SESSION_PERMANENT"] = False

        # Initialize CacheLib for enhanced session management
        cache = Cache()
        cache.init_app(app, config={
            "CACHE_TYPE": "FileSystemCache",
            "CACHE_DIR": "./flask_cache"
        })
        logger.info("Session management initialized successfully with CacheLib.")
    except Exception as e:
        logger.error(f"Failed to initialize session management: {e}")
        raise

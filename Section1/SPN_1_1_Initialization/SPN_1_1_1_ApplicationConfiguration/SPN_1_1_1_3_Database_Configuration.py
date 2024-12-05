# ===========================
# SPN_1_1_1_3_Database_Configuration
# Section: Core Setup
# Component: Initialization
# Module: Application Configuration
# Unit: Database Configuration
# Purpose: Establish a connection to the database.
# Input: Database URL and logger instance.
# Output: SQLAlchemy engine and session factory.
# ===========================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def configure_database(logger, db_url):
    """
    Configures the database connection using SQLAlchemy.

    Args:
        logger: Logger instance to log messages.
        db_url: Database connection URL.

    Returns:
        engine: SQLAlchemy engine instance.
        Session: SQLAlchemy session factory.
    """
    logger.info("Initializing database connection...")

    try:
        # Create SQLAlchemy engine
        engine = create_engine(db_url)
        logger.info("Database engine created successfully.")

        # Create a session factory
        Session = sessionmaker(bind=engine)
        logger.info("Session factory initialized successfully.")

        return engine, Session

    except Exception as e:
        logger.error(f"Failed to configure the database: {e}")
        raise

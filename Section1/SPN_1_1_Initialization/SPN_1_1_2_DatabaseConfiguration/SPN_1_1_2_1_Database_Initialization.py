# ===========================
# SPN_1_1_2_1_Database_Initialization
# Section: Core Setup
# Component: Initialization
# Module: Database Configuration
# Unit: Database Initialization
# Purpose: Initialize the database schema and tables.
# Input: SQLAlchemy engine instance.
# Output: Created database schema.
# ===========================

from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    """
    SQLAlchemy ORM model for the 'products' table.

    Attributes:
        id (Integer): Primary key for the product.
        name (String): Name of the product.
        description (String): Description of the product.
        price (Integer): Price of the product.
    """
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)

def initialize_database(engine, logger):
    """
    Initializes the database schema by creating all necessary tables.

    Args:
        engine: SQLAlchemy engine instance.
        logger: Logger instance to log messages.

    Returns:
        None
    """
    logger.info("Initializing database schema...")

    try:
        # Create all tables defined by the ORM
        Base.metadata.create_all(engine)
        logger.info("Database schema initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize the database schema: {e}")
        raise

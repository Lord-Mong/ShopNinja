# ===========================
# SPN_1_5_1_1_GoogleMerchantClient
# Section: Core Setup
# Component: ChannelSync
# Module: GoogleAPIClients
# Unit: GoogleMerchantClient
# Purpose: Establish connectivity and manage product data with Google Merchant Center API.
# ===========================

import json
import logging
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build  # Ensure this module is installed by running 'pip install google-api-python-client'

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GoogleMerchantClient:
    def __init__(self, credentials_file: str, merchant_id: str):
        """
        Initialize the Google Merchant Center client.
        :param credentials_file: Path to the service account credentials JSON file.
        :param merchant_id: Merchant ID for Google Merchant Center.
        """
        self.credentials_file = credentials_file
        self.merchant_id = merchant_id
        self.service = self.authenticate()

    def authenticate(self):
        """
        Authenticate using OAuth 2.0 credentials from a service account file.
        :return: Authorized service object.
        """
        try:
            logger.info("Authenticating with Google Merchant Center API...")
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_file,
                scopes=["https://www.googleapis.com/auth/content"]
            )
            # Use 'content' as the service name and 'v2.1' as the version
            service = build('content', 'v2.1', credentials=credentials)
            logger.info("Authentication successful.")
            return service
        except Exception as e:
            logger.error(f"Failed to authenticate with Google Merchant Center: {e}")
            raise

    def list_products(self):
        """
        List all products in the Google Merchant Center account.
        """
        try:
            request = self.service.products().list(merchantId=self.merchant_id)
            response = request.execute()
            logger.info("Fetched product list successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to list products: {e}")
            return None

    def insert_product(self, product_data: dict):
        """
        Insert a new product in the Google Merchant Center.
        :param product_data: Dictionary containing product details.
        """
        try:
            request = self.service.products().insert(
                merchantId=self.merchant_id,
                body=product_data
            )
            response = request.execute()
            logger.info("Product inserted successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to insert product: {e}")
            return None

    def update_product(self, product_id: str, updated_data: dict):
        """
        Update an existing product in the Google Merchant Center.
        :param product_id: ID of the product to be updated.
        :param updated_data: Dictionary containing updated product details.
        """
        try:
            request = self.service.products().update(
                merchantId=self.merchant_id,
                productId=product_id,
                body=updated_data
            )
            response = request.execute()
            logger.info("Product updated successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to update product: {e}")
            return None

    def delete_product(self, product_id: str):
        """
        Delete a product from the Google Merchant Center.
        :param product_id: ID of the product to be deleted.
        """
        try:
            request = self.service.products().delete(
                merchantId=self.merchant_id,
                productId=product_id
            )
            response = request.execute()
            logger.info("Product deleted successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to delete product: {e}")
            return None

# Example usage
if __name__ == "__main__":
    credentials_file_path = "G:/ShopNinja/shopninja-test-3fda0ea8a770.json"
    merchant_id = "5503304012"

    google_client = GoogleMerchantClient(credentials_file_path, merchant_id)

    # Test listing products
    products = google_client.list_products()
    if products:
        logger.info(f"Products: {json.dumps(products, indent=2)}")

    # Test inserting a product
    new_product_data = {
        "offerId": "12345",
        "title": "Test Product",
        "description": "This is a test product.",
        "link": "https://example.com/test-product",
        "imageLink": "https://example.com/test-product.jpg",
        "contentLanguage": "en",
        "targetCountry": "US",
        "channel": "online",
        "availability": "in stock",
        "condition": "new",
        "price": {
            "value": "29.99",
            "currency": "USD"
        }
    }

    inserted_product = google_client.insert_product(new_product_data)
    if inserted_product:
        logger.info(f"Inserted Product: {json.dumps(inserted_product, indent=2)}")

    # Test updating a product
    if inserted_product:
        product_id = inserted_product.get("id")  # Extract the product ID
        updated_product_data = {
            "title": "Updated Test Product",
            "description": "This is an updated test product.",
            "price": {
                "value": "24.99",
                "currency": "USD"
            }
        }
        updated_product = google_client.update_product(product_id, updated_product_data)
        if updated_product:
            logger.info(f"Updated Product: {json.dumps(updated_product, indent=2)}")

    # Test deleting a product
    if inserted_product:
        product_id = inserted_product.get("id")
        deleted_product = google_client.delete_product(product_id)
        if deleted_product:
            logger.info(f"Deleted Product ID: {product_id}")

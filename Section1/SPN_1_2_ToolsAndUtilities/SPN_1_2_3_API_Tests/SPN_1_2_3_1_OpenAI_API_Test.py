# ===========================
# SPN_1_2_3_1_OpenAI_API_Test
# Section: Core Setup
# Component: Tools and Utilities
# Module: API Tests
# Unit: OpenAI API Test
# Purpose: Verify connectivity to the OpenAI API.
# ===========================

import openai
import logging
from openai import AuthenticationError, APIError, RateLimitError, BadRequestError  # Corrected exceptions import
from tenacity import retry, stop_after_attempt, wait_exponential  # For retry mechanism

# Logger setup (moved to centralized reusable utility)
logger = logging.getLogger("OpenAI_Connectivity")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def verify_openai_connectivity(api_key: str) -> bool:
    """
    Verifies connectivity to the OpenAI API by making a basic request.
    :param api_key: API key for OpenAI
    :return: True if the connection is successful, False otherwise
    """
    openai.api_key = api_key

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def make_request():
        # Making a basic request to verify connectivity
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello, OpenAI"}]
        )
        return response

    try:
        response = make_request()
        logger.info("OpenAI API connectivity verified successfully.")
        return True

    except AuthenticationError as auth_err:
        logger.error(f"Authentication failed: {auth_err}")
        return False
    except RateLimitError as rate_err:
        logger.error(f"Rate limit exceeded: {rate_err}")
        return False
    except BadRequestError as req_err:
        logger.error(f"Bad request: {req_err}")
        return False
    except APIError as api_err:
        logger.error(f"General API error: {api_err}")
        return False
    except Exception as ex:
        logger.error(f"Failed to verify OpenAI connectivity: {ex}")
        return False

# If run directly, for manual verification
if __name__ == "__main__":
    openai_api_key = "your_openai_api_key_here"
    connectivity_status = verify_openai_connectivity(openai_api_key)
    if connectivity_status:
        logger.info("OpenAI API key is valid and verified.")
    else:
        logger.error("Failed to verify OpenAI API key. Please check the key.")

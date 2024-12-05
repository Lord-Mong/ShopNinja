# ===========================
# SPN_1_4_1_1_Fetch_Channel_Requirements
# Section: Core Setup
# Component: Channel Update Management
# Module: Channel Requirement Sync
# Unit: Fetch Channel Requirements
# Purpose: Fetch the latest channel-specific requirements via API calls.
# Input: API endpoints for each channel.
# Output: Raw channel requirements data.
# ===========================

import requests

def fetch_channel_requirements(logger, api_endpoints):
    """
    Fetch channel-specific requirements from given API endpoints.

    Args:
        logger: Logger instance to log messages.
        api_endpoints: Dictionary mapping channel names to API endpoint URLs.

    Returns:
        Dictionary mapping channel names to their fetched requirements, or None on failure.
    """
    results = {}
    for channel, endpoint in api_endpoints.items():
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise HTTPError for bad responses
            results[channel] = response.json()
            logger.info(f"Successfully fetched requirements for {channel}.")
        except Exception as e:
            logger.error(f"Failed to fetch requirements for {channel}: {e}")
            results[channel] = None
    return results


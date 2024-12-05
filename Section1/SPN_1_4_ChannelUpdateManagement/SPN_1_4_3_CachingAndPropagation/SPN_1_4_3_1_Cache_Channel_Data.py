# ===========================
# SPN_1_4_3_1_Cache_Channel_Data
# Section: Core Setup
# Component: Channel Update Management
# Module: Caching and Propagation
# Unit: Cache Channel Data
# Purpose: Cache updated channel requirements for efficient access.
# Input: Updated channel requirements.
# Output: Cache status or error message.
# ===========================

import os
import json

def cache_channel_data(logger, updated_requirements, cache_dir):
    """
    Caches updated channel requirements into JSON files.

    Args:
        logger: Logger instance to log messages.
        updated_requirements: Dictionary of updated channel requirements.
        cache_dir: Directory path to store cached requirements.

    Returns:
        True if caching is successful, False otherwise.
    """
    try:
        os.makedirs(cache_dir, exist_ok=True)
        for channel, requirements in updated_requirements.items():
            file_path = os.path.join(cache_dir, f"{channel}_requirements.json")
            with open(file_path, "w") as file:
                json.dump(requirements, file, indent=4)
            logger.info(f"Cached requirements for {channel} at {file_path}.")
        logger.info("All channel requirements successfully cached.")
        return True
    except Exception as e:
        logger.error(f"Failed to cache channel requirements: {e}")
        return False

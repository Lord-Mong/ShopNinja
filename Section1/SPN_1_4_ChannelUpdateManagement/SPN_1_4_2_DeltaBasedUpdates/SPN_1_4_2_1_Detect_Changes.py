# ===========================
# SPN_1_4_2_1_Detect_Changes
# Section: Core Setup
# Component: Channel Update Management
# Module: Delta-Based Updates
# Unit: Detect Changes
# Purpose: Compare current and newly fetched channel requirements to detect changes.
# Input: Current requirements, newly formatted requirements.
# Output: Detected changes as a dictionary.
# ===========================

def detect_changes(logger, current_requirements, new_requirements):
    """
    Detects changes between current and new channel requirements.

    Args:
        logger: Logger instance to log messages.
        current_requirements: Dictionary of current channel requirements.
        new_requirements: Dictionary of new channel requirements.

    Returns:
        Dictionary of detected changes for each channel.
    """
    changes = {}

    for channel, new_data in new_requirements.items():
        if not new_data:
            logger.warning(f"No new data for {channel}. Skipping change detection.")
            continue

        current_data = current_requirements.get(channel)
        if not current_data:
            # Entirely new channel
            changes[channel] = {
                "required_fields": {"added": new_data["required_fields"], "removed": []},
                "optional_fields": {"added": new_data.get("optional_fields", []), "removed": []},
                "last_updated": {"old": None, "new": new_data["last_updated"]}
            }
            logger.info(f"Detected changes for {channel}.")
            continue

        # Detect changes
        changes[channel] = {
            "required_fields": {
                "added": [field for field in new_data["required_fields"] if field not in current_data["required_fields"]],
                "removed": [field for field in current_data["required_fields"] if field not in new_data["required_fields"]],
            },
            "optional_fields": {
                "added": [field for field in new_data.get("optional_fields", []) if field not in current_data.get("optional_fields", [])],
                "removed": [field for field in current_data.get("optional_fields", []) if field not in new_data.get("optional_fields", [])],
            },
            "last_updated": {
                "old": current_data["last_updated"],
                "new": new_data["last_updated"],
            },
        }
        logger.info(f"Detected changes for {channel}.")

    return changes

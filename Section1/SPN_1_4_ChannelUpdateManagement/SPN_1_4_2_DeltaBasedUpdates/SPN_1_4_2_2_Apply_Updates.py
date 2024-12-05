# ===========================
# SPN_1_4_2_2_Apply_Updates
# Section: Core Setup
# Component: Channel Update Management
# Module: Delta-Based Updates
# Unit: Apply Updates
# Purpose: Apply detected changes to the stored channel requirements.
# Input: Detected changes and the current requirements.
# Output: Updated channel requirements.
# ===========================

def apply_updates(logger, current_requirements, changes):
    """
    Applies detected changes to the current channel requirements.

    Args:
        logger: Logger instance to log messages.
        current_requirements: Dictionary of current channel requirements.
        changes: Dictionary of detected changes to apply.

    Returns:
        Updated channel requirements.
    """
    for channel, change in changes.items():
        logger.info(f"Applying changes for {channel}.")
        if "required_fields" in change:
            added = change["required_fields"].get("added", [])
            removed = change["required_fields"].get("removed", [])
            current_requirements[channel]["required_fields"] = [
                field for field in current_requirements[channel]["required_fields"] if field not in removed
            ] + added
        if "optional_fields" in change:
            added = change["optional_fields"].get("added", [])
            removed = change["optional_fields"].get("removed", [])
            current_requirements[channel]["optional_fields"] = [
                field for field in current_requirements[channel]["optional_fields"] if field not in removed
            ] + added
        if "last_updated" in change:
            current_requirements[channel]["last_updated"] = change["last_updated"]["new"]

        logger.info(f"Updates applied for {channel}.")

    logger.info("All updates successfully applied.")
    return current_requirements

# ===========================
# SPN_1_4_3_2_Propagate_Updates
# Section: Core Setup
# Component: Channel Update Management
# Module: Caching and Propagation
# Unit: Propagate Updates
# Purpose: Propagate updated channel requirements to dependent modules or services.
# Input: Updated channel requirements and target modules.
# Output: Propagation status or error message.
# ===========================

def propagate_updates(logger, cached_requirements, target_systems):
    """
    Propagates cached channel requirements to target systems.

    Args:
        logger: Logger instance to log messages.
        cached_requirements: Dictionary of cached channel requirements.
        target_systems: Dictionary mapping system names to callable propagation functions.

    Returns:
        True if all updates are successfully propagated, False otherwise.
    """
    all_success = True

    for system_name, propagate_func in target_systems.items():
        try:
            if not callable(propagate_func):
                raise TypeError(f"Target system {system_name} is not callable.")

            success = propagate_func(cached_requirements)
            if success:
                logger.info(f"Successfully propagated updates to {system_name}.")
            else:
                logger.error(f"Failed to propagate updates to {system_name}.")
                all_success = False
        except Exception as e:
            logger.error(f"Error during propagation to {system_name}: {e}")
            all_success = False

    return all_success

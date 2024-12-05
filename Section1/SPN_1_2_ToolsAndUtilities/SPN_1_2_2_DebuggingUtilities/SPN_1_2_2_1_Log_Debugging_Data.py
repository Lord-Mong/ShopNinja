# ===========================
# SPN_1_2_2_1_Log_Debugging_Data
# Section: Core Setup
# Component: Tools & Utilities
# Module: Debugging Utilities
# Unit: Log Debugging Data
# Purpose: Logs debugging information to help trace application logic.
# Input: Context description and debug data.
# Output: Logged debugging information.
# ===========================

def log_debug_data(logger, context, debug_data):
    """
    Logs debugging information for troubleshooting.

    Args:
        logger: Logger instance to log messages.
        context (str): A description of the context or process being debugged.
        debug_data (any): The data to log for debugging purposes.

    Returns:
        None
    """
    try:
        logger.debug(f"[DEBUG] Context: {context}, Data: {debug_data}")
    except Exception as e:
        logger.error(f"[ERROR] Failed to log debug data: {e}")

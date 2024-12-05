# ===========================
# SPN_1_2_2_2_Performance_Profiler
# Section: Core Setup
# Component: Tools & Utilities
# Module: Debugging Utilities
# Unit: Performance Profiler
# Purpose: Profiles the performance of functions by logging execution times.
# Input: Function to profile.
# Output: Execution time logged.
# ===========================

import time

def performance_profiler(logger):
    """
    Decorator to measure and log the execution time of a function.

    Args:
        logger: Logger instance to log messages.

    Returns:
        Callable: A wrapped function with profiling applied.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.info(f"[PROFILE] {func.__name__} executed in {execution_time:.4f} seconds.")
            return result
        return wrapper
    return decorator

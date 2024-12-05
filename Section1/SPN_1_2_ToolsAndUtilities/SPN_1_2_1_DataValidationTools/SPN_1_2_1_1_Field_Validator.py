# ===========================
# SPN_1_2_1_1_Field_Validator
# Section: Core Setup
# Component: Tools & Utilities
# Module: Data Validation Tools
# Unit: Field Validator
# Purpose: Validate individual fields based on rules.
# Input: Field name, field value, and validation rules.
# Output: Validation result (boolean) and error messages (if any).
# ===========================

def validate_field(field_name, field_value, rules):
    """
    Validates a field against a set of rules.

    Args:
        field_name (str): The name of the field to validate.
        field_value (any): The value of the field to validate.
        rules (dict): A dictionary of validation rules (e.g., type, required, max_length).

    Returns:
        tuple: (bool, str) where the first value indicates success,
               and the second is an error message.
    """
    if "required" in rules and rules["required"] and not field_value:
        return False, f"{field_name} is required but not provided."

    if "type" in rules and not isinstance(field_value, rules["type"]):
        return False, f"{field_name} must be of type {rules['type'].__name__}."

    if "max_length" in rules and isinstance(field_value, str) and len(field_value) > rules["max_length"]:
        return False, f"{field_name} exceeds maximum length of {rules['max_length']}."

    return True, "Field is valid."

# ===========================
# SPN_1_2_1_2_Product_Data_Validator
# Section: Core Setup
# Component: Tools & Utilities
# Module: Data Validation Tools
# Unit: Product Data Validator
# Purpose: Validate product data dictionaries using field-level rules.
# Input: Product data dictionary and validation rules.
# Output: Validation results for all fields with status and errors.
# ===========================

from Section1.SPN_1_2_ToolsAndUtilities.SPN_1_2_1_DataValidationTools.SPN_1_2_1_1_Field_Validator import validate_field

def validate_product_data(product_data, field_rules):
    """
    Validates all fields in a product data dictionary.

    Args:
        product_data (dict): The product data dictionary to validate.
        field_rules (dict): A dictionary where keys are field names and values are validation rules.

    Returns:
        dict: Validation results for each field.
              Each key in the returned dictionary corresponds to a field,
              with its value being a dictionary containing:
                  - 'is_valid' (bool): Whether the field is valid.
                  - 'message' (str): Validation message or error.
    """
    validation_results = {}
    for field_name, rules in field_rules.items():
        field_value = product_data.get(field_name)
        is_valid, message = validate_field(field_name, field_value, rules)
        validation_results[field_name] = {
            "is_valid": is_valid,
            "message": message
        }
    return validation_results

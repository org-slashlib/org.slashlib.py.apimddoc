# -*- coding: utf-8 -*-
# file test/10_01_03_models_basemodel_is_root_model_test.py
# @AI:
# - INTEGRITY RULES:
#   - STRICT PRESERVATION: Do not remove, move, or modify ANY existing lines of code or comments 
#     unless they are the explicit target of the requested change. 
#   - DEBUG MARKERS: Commented-out code (e.g., debug prints) MUST be kept exactly where they are.
#   - WHITESPACE & STRUCTURE: Maintain all original empty lines and the existing file structure. 
#     Structural integrity takes precedence over "clean code" or "elegance".
#   - LEAD-IN/OUT: The very first and last lines (and all comments in between) are immutable anchors.
# - MAINTENANCE:
#   - Only update pydoc strings (args, returns, raises) if the function signature changes.
#   - Do NOT delete existing examples or descriptions in pydoc.
# - LANGUAGE: en-US for all comments and documentation.
#

"""
Module: models.py
Class: BaseModel
Method: is_root_model
Special Considerations: 
- Validates the logic that determines if a module is at the root level (no dots in FQMN).
"""

import pytest
from org.slashlib.py.apimddoc.core.models.basemodel import BaseModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(BaseModel), "BaseModel must be a class"

def test_is_root_model_true():
    """
    What: Verify that is_root_model returns True for root modules.
    Why: Ensure logic correctly identifies modules without nested namespaces.
    """
    instance = BaseModel(name="root", fqmn="root", file_path="root.py")
    assert instance.is_root_model() is True

def test_is_root_model_false():
    """
    What: Verify that is_root_model returns False for nested modules.
    Why: Ensure logic correctly identifies modules with nested namespaces.
    """
    instance = BaseModel(name="nested", fqmn="org.slashlib.nested", file_path="nested.py")
    assert instance.is_root_model() is False

# end of file test/10_01_03_models_basemodel_is_root_model_test.py
# -*- coding: utf-8 -*-
# file test/10_01_02_models_basemodel_fqmn_test.py
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
Method: fqmn (property getter and setter)
Special Considerations: 
- Validates the transformation logic between the string FQMN and the internal _fqmn_parts list.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.basemodel import BaseModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(BaseModel), "BaseModel must be a class"

def test_fqmn_getter_setter():
    """
    What: Verify that the fqmn property correctly sets and retrieves values.
    Why: Ensure the setter splits the string into parts and the getter joins them back correctly.
    """
    # Initialize with a dummy path
    instance = BaseModel(name="test", fqmn="a.b.c", file_path="test.py")
    
    # Test getter
    assert instance.fqmn == "a.b.c"
    
    # Test setter
    instance.fqmn = "org.slashlib.new"
    assert instance.fqmn == "org.slashlib.new"
    assert instance._fqmn_parts == ["org", "slashlib", "new"]

def test_fqmn_single_part():
    """
    What: Verify fqmn handling with a single part (root module).
    Why: Ensure no errors occur when there are no dots in the FQMN.
    """
    instance = BaseModel(name="root", fqmn="root", file_path="root.py")
    
    assert instance.fqmn == "root"
    assert instance._fqmn_parts == ["root"]

# end of file test/10_01_02_models_basemodel_fqmn_test.py
# -*- coding: utf-8 -*-
# file test/10_01_01_models_basemodel_init_test.py
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
Method: __init__
Special Considerations: 
- Validates correct attribute initialization.
- Verifies property fqmn correctly splits and joins parts.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.basemodel import BaseModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(BaseModel), "BaseModel must be a class"

def test_basemodel_init_success():
    """
    What: Verify successful initialization of BaseModel.
    Why: Ensure attributes are set correctly and property logic functions.
    """
    name = "test_entity"
    fqmn = "org.slashlib.test"
    file_path = "/path/to/file.py"
    
    instance = BaseModel(name=name, fqmn=fqmn, file_path=file_path)
    
    assert instance.name == name
    assert instance.fqmn == fqmn
    assert instance.file_path == file_path
    assert instance._fqmn_parts == ["org", "slashlib", "test"]

# end of file test/10_01_01_models_basemodel_init_test.py
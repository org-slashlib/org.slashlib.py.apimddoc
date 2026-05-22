# -*- coding: utf-8 -*-
# file test/06_01_04_registry_projectregistry_get_module_test.py
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
Module: registry.py
Class: ProjectRegistry
Method: get_module
Special Considerations: 
- Validates retrieval of modules by their Fully Qualified Module Name (FQMN).
"""

import pytest
from unittest.mock import MagicMock
from org.slashlib.py.apimddoc.core.registry import ProjectRegistry
from org.slashlib.py.apimddoc.core.models.basemodulemodel import BaseModuleModel

def test_get_module_found():
    """
    What: Verify that a registered module can be retrieved.
    Why: Ensure the registry correctly maps FQMN to the stored module instance.
    """
    fqmn = "org.slashlib.module"
    mock_module = MagicMock(spec=BaseModuleModel)
    
    # Manually register the module for the test
    ProjectRegistry.register_module(mock_module, fqmn)
    
    # Retrieve and verify
    result = ProjectRegistry.get_module(fqmn)
    assert result == mock_module, "The retrieved module should match the registered instance."

def test_get_module_not_found():
    """
    What: Verify that retrieving a non-existent module returns None.
    Why: Ensure safe handling of missing modules without raising exceptions.
    """
    result = ProjectRegistry.get_module("non.existent.fqmn")
    assert result is None, "Retrieving a non-existent FQMN should return None."

# end of file test/06_01_04_registry_projectregistry_get_module_test.py
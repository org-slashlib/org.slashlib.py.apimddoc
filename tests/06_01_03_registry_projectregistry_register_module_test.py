# -*- coding: utf-8 -*-
# file test/06_01_03_registry_projectregistry_register_module_test.py
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
Method: register_module
Special Considerations: 
- Validates that modules can be correctly registered and retrieved from the registry.
"""

import pytest
from unittest.mock import MagicMock
from org.slashlib.py.apimddoc.core.registry import ProjectRegistry
from org.slashlib.py.apimddoc.core.models.basemodulemodel import BaseModuleModel

def test_register_module_success():
    """
    What: Verify that a module can be registered and retrieved.
    Why: Ensure the internal dictionary maps the FQMN correctly to the module instance.
    """
    # Create a mock module instance
    mock_module = MagicMock(spec=BaseModuleModel)
    fqmn = "org.slashlib.test"
    
    # Perform registration
    ProjectRegistry.register_module(mock_module, fqmn)
    
    # Verify retrieval
    retrieved_module = ProjectRegistry.get_module(fqmn)
    assert retrieved_module == mock_module, "The registered module must be retrievable via its FQMN."

def test_get_nonexistent_module():
    """
    What: Verify behavior when retrieving a non-existent module.
    Why: Ensure that None is returned as expected.
    """
    assert ProjectRegistry.get_module("non.existent.module") is None, \
        "Retrieving a non-existent FQMN must return None."

# end of file test/06_01_03_registry_projectregistry_register_module_test.py
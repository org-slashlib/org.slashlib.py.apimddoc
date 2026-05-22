# -*- coding: utf-8 -*-
# file test/06_01_06_registry_projectregistry_list_all_modules_test.py
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
Method: list_all_modules
Special Considerations: 
- Validates that all registered modules are returned in the list.
"""

import pytest
from unittest.mock import MagicMock
from org.slashlib.py.apimddoc.core.registry import ProjectRegistry
from org.slashlib.py.apimddoc.core.models.basemodulemodel import BaseModuleModel

@pytest.fixture(autouse=True)
def clean_registry():
    """Fixture to ensure the registry is empty before each test."""
    ProjectRegistry._modules = {}
    yield

def test_list_all_modules():
    """
    What: Verify that list_all_modules returns all registered module models.
    Why: Ensure that the registry correctly exposes its full content.
    """
    # Setup
    mod1 = MagicMock(spec=BaseModuleModel)
    mod2 = MagicMock(spec=BaseModuleModel)
    
    ProjectRegistry.register_module(mod1, "module.one")
    ProjectRegistry.register_module(mod2, "module.two")
    
    # Retrieve
    all_modules = ProjectRegistry.list_all_modules()
    
    # Assertions
    assert len(all_modules) == 2, f"Expected 2 modules, found {len(all_modules)}"
    assert mod1 in all_modules, "The first registered module should be in the list."
    assert mod2 in all_modules, "The second registered module should be in the list."

# end of file test/06_01_06_registry_projectregistry_list_all_modules_test.py
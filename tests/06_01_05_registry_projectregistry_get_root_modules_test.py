# -*- coding: utf-8 -*-
# file test/06_01_05_registry_projectregistry_get_root_modules_test.py
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
Method: get_root_modules
Special Considerations: 
- Validates that only top-level modules are returned.
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

def test_get_root_modules_filtering():
    """
    What: Verify that get_root_modules returns only modules without a '.' in FQMN.
    Why: Ensure the filtering logic correctly identifies top-level packages/modules.
    """
    # Setup: Register different types of modules
    root_mod = MagicMock(spec=BaseModuleModel)
    sub_mod = MagicMock(spec=BaseModuleModel)
    
    ProjectRegistry.register_module(root_mod, "root")
    ProjectRegistry.register_module(sub_mod, "root.sub")
    
    # Retrieve root modules
    roots = ProjectRegistry.get_root_modules()
    
    # Assertions
    assert len(roots) == 1, f"Expected 1 root module, but found {len(roots)}: {roots}"
    assert roots[0] == root_mod, "The root module should be the one without a dot in its FQMN."
    assert sub_mod not in roots, "Sub-modules should not be returned by get_root_modules."

# end of file test/06_01_05_registry_projectregistry_get_root_modules_test.py
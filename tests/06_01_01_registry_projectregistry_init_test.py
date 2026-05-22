# -*- coding: utf-8 -*-
# file test/06_01_01_registry_projectregistry_init_test.py
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
Method: _class_auto_init_
Special Considerations: 
- Validates that the metaclass AutoInitializer successfully triggers 
  _class_auto_init_ upon class loading.
"""

import pytest
from org.slashlib.py.apimddoc.core.registry import ProjectRegistry

def test_registry_auto_initialization():
    """
    What: Verify that ProjectRegistry initializes its state automatically.
    Why: Ensure that the metaclass integration correctly sets up the registry
         storage and initialization flag upon definition.
    """
    # Access private attributes to verify the initialization state.
    # __is_initialized is mangled to _ProjectRegistry__is_initialized
    assert ProjectRegistry._ProjectRegistry__is_initialized is True, \
        "The registry must be marked as initialized after class creation."
    
    # Ensure the storage dictionary is created
    assert ProjectRegistry._modules == {}, \
        "The registry module storage must be an empty dictionary upon initialization."

def test_registry_manual_auto_init_call():
    """
    What: Verify that _class_auto_init_ can be called manually without breaking state.
    Why: Ensure the idempotency check (if __is_initialized return) works as expected.
    """
    # Simulate a state change (add a dummy entry)
    dummy_module = "dummy"
    ProjectRegistry._modules["test"] = dummy_module
    
    # Manually trigger the auto-init method
    ProjectRegistry._class_auto_init_()
    
    # Check if the state is preserved (because it was already initialized)
    assert ProjectRegistry._ProjectRegistry__is_initialized is True
    assert ProjectRegistry._modules["test"] == dummy_module, \
        "Manual call should not reset _modules if already initialized."

# end of file test/06_01_01_registry_projectregistry_init_test.py
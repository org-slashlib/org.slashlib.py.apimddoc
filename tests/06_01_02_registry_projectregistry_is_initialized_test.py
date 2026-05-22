# -*- coding: utf-8 -*-
# file test/06_01_02_registry_projectregistry_is_initialized_test.py
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
Method: is_initialized
Special Considerations: 
- Validates the public initialization status of the ProjectRegistry.
"""

import pytest
from org.slashlib.py.apimddoc.core.registry import ProjectRegistry

def test_registry_is_initialized_method():
    """
    What: Verify that the is_initialized() method returns the correct state.
    Why: Ensure that the public API for checking initialization works correctly
         after the metaclass has processed the class definition.
    """
    # Wir rufen die Methode is_initialized() auf, statt auf das private Attribut zuzugreifen
    assert ProjectRegistry.is_initialized() is True, \
        "The registry must report its initialized state correctly via is_initialized()."

# end of file test/06_01_02_registry_projectregistry_is_initialized_test.py
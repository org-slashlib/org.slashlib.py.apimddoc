# -*- coding: utf-8 -*-
# file test/05_01_01_meta_autoinitializer_init_test.py
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
Module: meta.py
Class: AutoInitializer
Method: __init__
Special Considerations: 
- Validates that the metaclass correctly triggers _class_auto_init_ upon class creation.
- Tests validation logic for the _class_auto_init_ method definition.
"""

import pytest
from org.slashlib.py.apimddoc.meta import AutoInitializer

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the metaclass is importable.
    """
    assert isinstance(AutoInitializer, type), "AutoInitializer must be a metaclass"

def test_auto_init_trigger_success():
    """
    What: Verify that _class_auto_init_ is triggered upon class definition.
    Why: Ensure the metaclass correctly inspects and executes the initialization hook.
    """
    class TestInit(metaclass=AutoInitializer):
        initialized = False
        
        @classmethod
        def _class_auto_init_(cls):
            cls.initialized = True
            
    assert TestInit.initialized is True

def test_auto_init_raises_type_error_for_non_classmethod():
    """
    What: Verify that TypeError is raised if _class_auto_init_ is not a classmethod.
    Why: Ensure the metaclass enforces the correct signature for the hook.
    """
    with pytest.raises(TypeError, match="must be a classmethod"):
        class InvalidInit(metaclass=AutoInitializer):
            def _class_auto_init_(self):
                pass

# end of file test/05_01_01_meta_autoinitializer_init_test.py
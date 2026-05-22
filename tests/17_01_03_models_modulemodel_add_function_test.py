# -*- coding: utf-8 -*-
# file test/17_01_03_models_modulemodel_add_function_test.py
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
Module: modulemodel.py
Class: ModuleModel
Method: add_function
Special Considerations: 
- Validates that a FunctionModel instance can be correctly added to the module's functions list.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.modulemodel import ModuleModel
from org.slashlib.py.apimddoc.core.models.functionmodel import FunctionModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(ModuleModel), "ModuleModel must be a class"

def test_add_function_success():
    """
    What: Verify that a function is correctly added to the functions list.
    Why: Ensure the internal list state is updated properly when a function is added.
    """
    parent_module = ModuleModel(
        name="test_mod", 
        fqmn="org.test", 
        file_path="test.py", 
        display_namespace="Test", 
        source_namespace="Test"
    )
    
    func = FunctionModel(
        name="my_func", 
        fqmn="org.test.my_func", 
        file_path="test.py", 
        source_namespace="Test",
        display_namespace="Test"
    )
    
    parent_module.add_function(func)
    
    assert len(parent_module.functions) == 1
    assert parent_module.functions[0] == func
    assert parent_module.functions[0].name == "my_func"

# end of file test/17_01_03_models_modulemodel_add_function_test.py
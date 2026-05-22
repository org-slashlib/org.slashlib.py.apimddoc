# -*- coding: utf-8 -*-
# file test/12_01_02_models_classmodel_add_method_test.py
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
Module: classmodel.py
Class: ClassModel
Method: add_method
Special Considerations: 
- Validates that a FunctionModel instance can be correctly added to the class's methods list.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.classmodel import ClassModel
from org.slashlib.py.apimddoc.core.models.functionmodel import FunctionModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(ClassModel), "ClassModel must be a class"

def test_add_method_success():
    """
    What: Verify that a method is correctly added to the methods list.
    Why: Ensure the internal list state is updated properly when a method is added.
    """
    # Create ClassModel instance
    parent_class = ClassModel(
        name="TestClass", 
        fqmn="org.test", 
        file_path="test.py", 
        canonical_path="org.test.TestClass", 
        display_namespace="Test", 
        source_namespace="Test"
    )
    
    # Create FunctionModel instance (dummy parameters)
    method = FunctionModel(
        name="my_method", 
        fqmn="org.test.my_method", 
        file_path="test.py", 
        source_namespace="Test",
        display_namespace="Test"
    )
    
    # Add method
    parent_class.add_method(method)
    
    # Verify
    assert len(parent_class.methods) == 1
    assert parent_class.methods[0] == method
    assert parent_class.methods[0].name == "my_method"

# end of file test/12_01_02_models_classmodel_add_method_test.py
# -*- coding: utf-8 -*-
# file test/12_01_03_models_classmodel_add_property_test.py
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
Method: add_property
Special Considerations: 
- Validates that a PropertyModel instance can be correctly added to the class's properties list.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.classmodel import ClassModel
from org.slashlib.py.apimddoc.core.models.propertymodel import PropertyModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(ClassModel), "ClassModel must be a class"

def test_add_property_success():
    """
    What: Verify that a property is correctly added to the properties list.
    Why: Ensure the internal list state is updated properly when a property is added.
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
    
    # Create PropertyModel instance (dummy parameters)
    prop = PropertyModel(
        name="my_property", 
        fqmn="org.test.my_property", 
        file_path="test.py", 
        source_namespace="Test"
    )
    
    # Add property
    parent_class.add_property(prop)
    
    # Verify
    assert len(parent_class.properties) == 1
    assert parent_class.properties[0] == prop
    assert parent_class.properties[0].name == "my_property"

# end of file test/12_01_03_models_classmodel_add_property_test.py
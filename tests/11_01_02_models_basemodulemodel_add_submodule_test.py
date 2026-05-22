# -*- coding: utf-8 -*-
# file test/11_01_02_models_basemodulemodel_add_submodule_test.py
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
Module: basemodulemodel.py
Class: BaseModuleModel
Method: add_submodule
Special Considerations: 
- Validates that a BaseModuleModel can correctly be added to the submodules list of another instance.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.basemodulemodel import BaseModuleModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(BaseModuleModel), "BaseModuleModel must be a class"

def test_add_submodule_success():
    """
    What: Verify that a submodule is correctly added to the submodules list.
    Why: Ensure the internal list state is updated properly.
    """
    # Create parent module
    parent = BaseModuleModel(
        name="parent", 
        fqmn="root", 
        file_path="root.py", 
        display_namespace="Root", 
        source_namespace="Root"
    )
    
    # Create child module
    child = BaseModuleModel(
        name="child", 
        fqmn="root.child", 
        file_path="child.py", 
        display_namespace="Child", 
        source_namespace="Child"
    )
    
    # Add submodule
    parent.add_submodule(child)
    
    # Verify
    assert len(parent.submodules) == 1
    assert parent.submodules[0] == child
    assert parent.submodules[0].name == "child"

# end of file test/11_01_02_models_basemodulemodel_add_submodule_test.py
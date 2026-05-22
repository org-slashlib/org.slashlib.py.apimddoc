# -*- coding: utf-8 -*-
# file test/17_01_01_models_modulemodel_init_test.py
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
Method: __init__
Special Considerations: 
- Validates the correct initialization of the ModuleModel, including inherited attributes
  from BaseModuleModel and the initialization of module-specific collections.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.modulemodel import ModuleModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(ModuleModel), "ModuleModel must be a class"

def test_modulemodel_init_success():
    """
    What: Verify successful initialization of ModuleModel.
    Why: Ensure all inherited attributes and new collection attributes (classes, functions, 
         exported_names) are correctly initialized to their default empty states.
    """
    params = {
        "name": "test_module",
        "fqmn": "org.slashlib.module",
        "file_path": "/path/to/module.py",
        "display_namespace": "DisplayNS",
        "source_namespace": "SourceNS"
    }
    
    instance = ModuleModel(**params)
    
    # Assert inherited attributes
    assert instance.name == params["name"]
    assert instance.fqmn == params["fqmn"]
    assert instance.file_path == params["file_path"]
    assert instance.display_namespace == params["display_namespace"]
    assert instance.source_namespace == params["source_namespace"]
    
    # Assert specific ModuleModel attributes
    assert instance.classes == {}
    assert instance.functions == []
    assert instance.exported_names == set()

# end of file test/17_01_01_models_modulemodel_init_test.py
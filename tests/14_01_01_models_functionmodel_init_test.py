# -*- coding: utf-8 -*-
# file test/14_01_01_models_functionmodel_init_test.py
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
Module: functionmodel.py
Class: FunctionModel
Method: __init__
Special Considerations: 
- Validates the correct initialization of the FunctionModel, including inherited attributes
  from SignatureModel and BaseModel.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.functionmodel import FunctionModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(FunctionModel), "FunctionModel must be a class"

def test_functionmodel_init_success():
    """
    What: Verify successful initialization of FunctionModel.
    Why: Ensure all inherited attributes and specific FunctionModel 
         attributes are correctly initialized.
    """
    params = {
        "name": "test_function",
        "fqmn": "org.slashlib.test_function",
        "file_path": "/path/to/function.py",
        "source_namespace": "SourceNS",
        "display_namespace": "DisplayNS"
    }
    
    instance = FunctionModel(**params)
    
    # Assert inherited attributes
    assert instance.name == params["name"]
    assert instance.fqmn == params["fqmn"]
    assert instance.file_path == params["file_path"]
    assert instance.source_namespace == params["source_namespace"]
    
    # Assert specific FunctionModel attributes
    assert instance.display_namespace == params["display_namespace"]
    assert instance.parameters == []

# end of file test/14_01_01_models_functionmodel_init_test.py
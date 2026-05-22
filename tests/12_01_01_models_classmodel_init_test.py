# -*- coding: utf-8 -*-
# file test/12_01_01_models_classmodel_init_test.py
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
Method: __init__
Special Considerations: 
- Validates the correct initialization of the ClassModel, including inherited attributes
  from BaseModel and specific class-related metadata.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.classmodel import ClassModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(ClassModel), "ClassModel must be a class"

def test_classmodel_init_success():
    """
    What: Verify successful initialization of ClassModel.
    Why: Ensure all inherited attributes (BaseModel) and specific ClassModel 
         attributes are correctly initialized.
    """
    params = {
        "name": "TestClass",
        "fqmn": "org.slashlib.test",
        "file_path": "/path/to/test.py",
        "canonical_path": "org.slashlib.test.TestClass",
        "display_namespace": "DisplayNS",
        "source_namespace": "SourceNS"
    }
    
    instance = ClassModel(**params)
    
    # Assert inherited attributes
    assert instance.name == params["name"]
    assert instance.fqmn == params["fqmn"]
    assert instance.file_path == params["file_path"]
    
    # Assert specific ClassModel attributes
    assert instance.canonical_path == params["canonical_path"]
    assert instance.display_namespace == params["display_namespace"]
    assert instance.source_namespace == params["source_namespace"]
    assert instance.docstring is None
    assert instance.is_public is False
    assert instance.methods == []
    assert instance.properties == []

# end of file test/12_01_01_models_classmodel_init_test.py
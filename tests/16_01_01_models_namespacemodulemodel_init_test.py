# -*- coding: utf-8 -*-
# file test/16_01_01_models_namespacemodulemodel_init_test.py
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
Module: namespacemodulemodel.py
Class: NamespaceModuleModel
Method: __init__
Special Considerations: 
- Validates the correct initialization of the NamespaceModuleModel, including inherited 
  attributes from BaseModuleModel, BaseModel, and the specific module structure.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.namespacemodulemodel import NamespaceModuleModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(NamespaceModuleModel), "NamespaceModuleModel must be a class"

def test_namespacemodulemodel_init_success():
    """
    What: Verify successful initialization of NamespaceModuleModel.
    Why: Ensure all inherited attributes and parameters are correctly assigned to the instance.
    """
    params = {
        "name": "namespace_pkg",
        "fqmn": "org.slashlib.ns",
        "file_path": "/path/to/namespace_pkg",
        "display_namespace": "DisplayNS",
        "source_namespace": "SourceNS"
    }
    
    instance = NamespaceModuleModel(**params)
    
    # Assert inherited attributes (BaseModel/BaseModuleModel)
    assert instance.name == params["name"]
    assert instance.fqmn == params["fqmn"]
    assert instance.file_path == params["file_path"]
    
    # Assert BaseModuleModel specific attributes
    assert instance.display_namespace == params["display_namespace"]
    assert instance.source_namespace == params["source_namespace"]
    assert instance.docstring is None
    assert instance.submodules == []

# end of file test/16_01_01_models_namespacemodulemodel_init_test.py
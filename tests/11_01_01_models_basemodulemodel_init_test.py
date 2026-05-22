# -*- coding: utf-8 -*-
# file test/11_01_01_models_basemodulemodel_init_test.py
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
Method: __init__
Special Considerations: 
- Validates the correct initialization of the BaseModuleModel, including attributes inherited from BaseModel.
"""

import pytest
from org.slashlib.py.apimddoc.core.models.basemodulemodel import BaseModuleModel

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(BaseModuleModel), "BaseModuleModel must be a class"

def test_basemodulemodel_init_success():
    """
    What: Verify successful initialization of BaseModuleModel.
    Why: Ensure inherited and new attributes are correctly assigned.
    """
    name = "module_test"
    fqmn = "org.slashlib.module"
    file_path = "/path/to/module.py"
    display_ns = "DisplayNS"
    source_ns = "SourceNS"
    
    instance = BaseModuleModel(
        name=name, 
        fqmn=fqmn, 
        file_path=file_path, 
        display_namespace=display_ns, 
        source_namespace=source_ns
    )
    
    # Assert inherited attributes
    assert instance.name == name
    assert instance.fqmn == fqmn
    assert instance.file_path == file_path
    
    # Assert specific module attributes
    assert instance.display_namespace == display_ns
    assert instance.source_namespace == source_ns
    assert instance.docstring is None
    assert instance.submodules == []

# end of file test/11_01_01_models_basemodulemodel_init_test.py
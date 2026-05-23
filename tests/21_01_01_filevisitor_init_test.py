# -*- coding: utf-8 -*-
# file test/21_01_01_filevisitor_init_test.py
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

import pathlib
import pytest
from org.slashlib.py.apimddoc.parser.filevisitor import FileVisitor
from org.slashlib.py.apimddoc.core.models.modulemodel import ModuleModel

def test_filevisitor_init():
    """
    What: Test the initialization of FileVisitor.
    Why: Verify that the module_model is correctly assigned and current_class is initialized to None.
    """
    # Create a minimal ModuleModel as required by FileVisitor.__init__
    dummy_model = ModuleModel(
        name="test_module",
        fqmn="test_module",
        file_path=pathlib.Path("test.py"),
        display_namespace="test",
        source_namespace="test"
    )
    
    # Instantiate visitor
    visitor = FileVisitor(dummy_model)
    
    # Assert state
    assert visitor.module_model == dummy_model
    assert visitor.current_class is None
    
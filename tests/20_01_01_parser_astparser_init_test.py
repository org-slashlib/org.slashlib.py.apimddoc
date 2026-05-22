# -*- coding: utf-8 -*-
# file test/20_01_01_parser_astparser_init_test.py
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
Module: parser.py
Class: ASTParser
Method: __init__
Special Considerations: 
- Validates that the ASTParser is correctly initialized with the provided root path.
"""

import pytest
import pathlib
from org.slashlib.py.apimddoc.parser.parser import ASTParser

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the class is importable and callable.
    """
    assert callable(ASTParser), "ASTParser must be a class"

def test_astparser_init_success():
    """
    What: Verify successful initialization of ASTParser.
    Why: Ensure the root_path attribute is correctly assigned.
    """
    root_path = pathlib.Path("/tmp/test_project")
    parser = ASTParser(root_path=root_path)
    
    assert parser.root_path == root_path
    assert isinstance(parser.root_path, pathlib.Path)

# end of file test/20_01_01_parser_astparser_init_test.py
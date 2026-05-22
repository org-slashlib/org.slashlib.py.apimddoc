# -*- coding: utf-8 -*-
# file test/20_01_02_parser_astparser_parse_path_test.py
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
Method: parsePath
Special Considerations: 
- Validates the recursive path traversal logic.
"""

import pytest
import pathlib
from unittest.mock import MagicMock
from org.slashlib.py.apimddoc.parser.parser import ASTParser
from org.slashlib.py.apimddoc.core.registry import ProjectRegistry

def test_import_integrity():
    """Verify the integrity of the test object."""
    assert callable(ASTParser), "ASTParser must be a class"

def test_parse_path_delegation():
    """
    What: Verify that parsePath delegates correctly.
    Why: Ensure the path is split and passed to path segments logic.
    """
    root_path = pathlib.Path("/tmp/proj")
    parser = ASTParser(root_path=root_path)
    
    # Mocking internal logic to verify delegation
    parser.parsePathSegment = MagicMock()
    
    # Simulate a path
    target_path = pathlib.Path("/tmp/proj/module/sub")
    parser.parsePath(target_path)
    
    # Assert that parsePathSegment was called for the segments
    assert parser.parsePathSegment.called

def test_parse_path_respects_src_as_root():
    """
    What: Verify that 'src' is treated as the root boundary.
    Why: The parser should start registering modules only *after* 'src', 
         ensuring 'src' itself is not part of the FQMN.
    """
    # Setup: root points to 'src'
    src_root = pathlib.Path("/project/src")
    parser = ASTParser(root_path=src_root)
    
    # Simulate a file path inside the project
    file_path = src_root / "org" / "slashlib" / "test.py"
    
    # Process
    parser.parsePath(file_path)
    
    # Assertions
    # 'src' should not be registered as a module
    assert ProjectRegistry.get_module("src") is None
    # 'org' and subsequent parts should be registered
    assert ProjectRegistry.get_module("org") is not None
    assert ProjectRegistry.get_module("org.slashlib") is not None

# end of file test/20_01_02_parser_astparser_parse_path_test.py
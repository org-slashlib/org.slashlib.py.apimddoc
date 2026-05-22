# -*- coding: utf-8 -*-
# file test/20_01_02_parser_astparser_parse_test.py
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
Method: parse
Special Considerations: 
- Validates the orchestration of parsePath and parseFile.
"""

import pytest
import pathlib
from unittest.mock import MagicMock, patch
from org.slashlib.py.apimddoc.parser.parser import ASTParser
from org.slashlib.py.apimddoc.core.registry import ProjectRegistry

@pytest.fixture(autouse=True)
def clean_registry():
    """Ensure registry is fresh for orchestration testing."""
    ProjectRegistry._modules = {}
    yield

def test_parse_orchestration():
    """
    What: Verify that parse() calls both parsePath and parseFile for each file.
    Why: Ensure that the parsing process is correctly coordinated.
    """
    # Setup
    root_path = pathlib.Path("/project")
    parser = ASTParser(root_path=root_path)
    
    # Mock the internal methods
    parser.parsePath = MagicMock()
    parser.parseFile = MagicMock()
    
    file_list = [pathlib.Path("/project/mod.py")]
    
    # Execute
    parser.parse(file_list)
    
    # Assertions
    parser.parsePath.assert_called_once_with(file_list[0])
    parser.parseFile.assert_called_once_with(file_list[0])

# end of file test/20_01_02_parser_astparser_parse_test.py
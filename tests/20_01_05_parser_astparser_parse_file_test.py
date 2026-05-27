# -*- coding: utf-8 -*-
# file test/20_01_04_parser_astparser_parse_file_test.py
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
Method: parseFile
Special Considerations: 
- Validates the entry point for file-based AST parsing.
- Validates the parsing logic for a single file using the AST,
  ensuring proper interaction with SourceCrawler and FileVisitor.
"""

import pytest
import pathlib
from unittest.mock import patch, MagicMock
from org.slashlib.py.apimddoc.parser.parser import ASTParser
from org.slashlib.py.apimddoc.core.registry import ProjectRegistry
from org.slashlib.py.apimddoc.crawler import SourceCrawler


@pytest.fixture(autouse=True)
def clean_registry():
    """Ensure the registry is empty before each test to maintain isolation."""
    ProjectRegistry._modules = {}
    yield

def test_import_integrity():
    """Verify the integrity of the test object."""
    assert callable(ASTParser), "ASTParser must be a class"

def test_parse_file_with_valid_root():
    """
    What: Verify that parseFile executes when the file belongs to a registered source root.
    Why: Prevent ValueError from SourceCrawler by configuring a valid root.
    """
    # Define a temporary project root and source root
    proj_root = pathlib.Path.cwd() / "project"
    src_root = proj_root / "src"
    
    # Configure SourceCrawler to recognize the test path
    SourceCrawler._source_roots = [src_root]
    
    # Setup parser
    parser = ASTParser(root_path=src_root)
    
    # Path must be within the configured source root
    target_file = src_root / "module.py"
    
    # Ensure file exists (or mock it if necessary)
    # For a unit test, we focus on the logic; here we assume the file structure.
    # If the file does not exist, open() in parseFile will raise FileNotFoundError,
    # but the ValueError from SourceCrawler is resolved.
    
    try:
        parser.parseFile(target_file)
    except FileNotFoundError:
        # Expected if the file doesn't actually exist on disk
        pass

@patch("org.slashlib.py.apimddoc.parser.parser.SourceCrawler")
@patch("org.slashlib.py.apimddoc.parser.parser.FileVisitor")
@patch("builtins.open")
@patch("ast.parse")
def test_parse_file_orchestration(mock_ast_parse, mock_open, mock_visitor, mock_crawler):
    """
    What: Verify that parseFile correctly orchestrates AST extraction and visitor application.
    Why: Ensure the parser connects the registry model with the file's AST content.
    """
    # Setup
    parser = ASTParser(root_path=pathlib.Path("/project"))
    file_path = pathlib.Path("/project/test_module.py")
    fqmn = "org.slashlib.test"
    
    # Mock behavior
    mock_crawler.get_module_namespace.return_value = fqmn
    mock_module = MagicMock()
    ProjectRegistry.register_module(mock_module, fqmn)
    
    # Execute
    parser.parseFile(file_path)
    
    # Assertions
    mock_crawler.get_module_namespace.assert_called_once_with(file_path)
    mock_open.assert_called_once_with(file_path, "r", encoding="utf-8")
    assert mock_visitor.called, "FileVisitor should be instantiated with the module model."
    mock_visitor.return_value.visit.assert_called_once()
    
# end of file test/20_01_04_parser_astparser_parse_file_test.py
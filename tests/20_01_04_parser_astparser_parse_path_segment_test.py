# -*- coding: utf-8 -*-
# file test/20_01_03_parser_astparser_parse_path_segment_test.py
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
Method: parsePathSegment
Special Considerations: 
- Validates registry updates and branch logic (Module vs. Namespace) during segment parsing.
"""

import pytest
import pathlib
from unittest.mock import patch
from org.slashlib.py.apimddoc.parser.parser import ASTParser
from org.slashlib.py.apimddoc.core.registry import ProjectRegistry
from org.slashlib.py.apimddoc.core.models.modulemodel import ModuleModel
from org.slashlib.py.apimddoc.core.models.namespacemodulemodel import NamespaceModuleModel

def test_import_integrity():
    """Verify the integrity of the test object."""
    assert callable(ASTParser), "ASTParser must be a class"

@patch('org.slashlib.py.apimddoc.parser.parser.SourceCrawler.is_package', return_value=True)
def test_parse_path_segment_creates_module_model(mock_is_package):
    """
    What: Verify ModuleModel creation when crawler identifies a package.
    Why: Ensure branching logic correctly handles packages.
    """
    root_path = pathlib.Path("/tmp/proj")
    parser = ASTParser(root_path=root_path)
    
    module = parser.parsePathSegment(
        segment="pkg",
        index=0,
        segments=["pkg"],
        file_path=root_path / "pkg" / "file.py",
        current_fqmn_parts=[],
        parent_module=None
    )
    
    assert isinstance(module, ModuleModel)
    assert module.name == "pkg"
    assert ProjectRegistry.get_module("pkg") == module

@patch('org.slashlib.py.apimddoc.parser.parser.SourceCrawler.is_package', return_value=False)
def test_parse_path_segment_creates_namespace_model(mock_is_package):
    """
    What: Verify NamespaceModuleModel creation when crawler identifies a namespace.
    Why: Ensure branching logic correctly handles namespace packages.
    """
    root_path = pathlib.Path("/tmp/proj")
    parser = ASTParser(root_path=root_path)
    
    module = parser.parsePathSegment(
        segment="ns",
        index=0,
        segments=["ns"],
        file_path=root_path / "ns" / "file.py",
        current_fqmn_parts=[],
        parent_module=None
    )
    
    assert isinstance(module, NamespaceModuleModel)
    assert module.name == "ns"
    assert ProjectRegistry.get_module("ns") == module

# end of file test/20_01_03_parser_astparser_parse_path_segment_test.py
# -*- coding: utf-8 -*-
# file test/02_01_04_crawler_sourcecrawler_get_module_namespace_test.py
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
Module: crawler.py
Class: SourceCrawler
Method: get_module_namespace

Special Considerations:
- This test suite ensures the Crawler correctly maps file paths to Python module namespaces.
- Design Decisions regarding ignored scenarios:
    1. External Project Paths (e.g., ['../outside_root']): Ignored. 
       The tool does not validate external path security; it trusts the config.
    2. System/Dependency State: Ignored. 
       The environment setup is the responsibility of the host, not the tool.
"""

import pytest
import pathlib
from org.slashlib.py.apimddoc.crawler import SourceCrawler

def test_get_module_namespace_success(monkeypatch, tmp_path):
    """
    What: Verify correct namespace conversion.
    Why: Ensure nested files and package markers are handled correctly.
    """
    src = tmp_path / "src"
    src.mkdir()
    
    # State injection
    SourceCrawler._source_roots = (src,)
    
    # Test case 1: Regular file
    file_path = src / "pkg" / "module.py"
    assert SourceCrawler.get_module_namespace(file_path) == "pkg.module"
    
    # Test case 2: __init__ file
    init_path = src / "pkg" / "__init__.py"
    assert SourceCrawler.get_module_namespace(init_path) == "pkg"

def test_get_module_namespace_outside_root_failure(monkeypatch, tmp_path):
    """
    What: Verify that files outside of source roots cause an error.
    Why: Ensure strict path scoping.
    """
    src = tmp_path / "src"
    src.mkdir()
    outside = tmp_path / "outside.py"
    outside.touch()
    
    SourceCrawler._source_roots = (src,)
    
    with pytest.raises(ValueError):
        SourceCrawler.get_module_namespace(outside)

# end of file test/02_01_04_crawler_sourcecrawler_get_module_namespace_test.py
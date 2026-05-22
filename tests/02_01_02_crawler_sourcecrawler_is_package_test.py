# -*- coding: utf-8 -*-
# file test/02_01_02_crawler_sourcecrawler_is_package_test.py
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
Method: is_package

Special Considerations:
- This test suite verifies the identification of Python packages.
- Design Decisions:
    1. Filesystem Isolation: Uses tmp_path to create real directory structures
       to ensure accurate interaction with `pathlib` and `exists()` checks.
"""

import pytest
import pathlib
from org.slashlib.py.apimddoc.crawler import SourceCrawler

def test_sourcecrawler_is_package_integrity():
    """
    What: Verify the integrity of the test object (importability and type check).
    Why: Mandatory first test for every Testsuite.
    """
    assert SourceCrawler is not None
    assert isinstance(SourceCrawler, type)

def test_sourcecrawler_is_package_true(tmp_path):
    """
    What: Verify that a directory containing __init__.py is identified as a package.
    Why: Ensure the package detection logic correctly validates presence of __init__.py.
    """
    pkg_dir = tmp_path / "my_package"
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").touch()
    
    assert SourceCrawler.is_package(pkg_dir) is True

def test_sourcecrawler_is_package_false_no_init(tmp_path):
    """
    What: Verify that a directory without __init__.py is NOT identified as a package.
    Why: Ensure strict enforcement of Python package rules.
    """
    dir_path = tmp_path / "plain_directory"
    dir_path.mkdir()
    
    assert SourceCrawler.is_package(dir_path) is False

def test_sourcecrawler_is_package_false_file(tmp_path):
    """
    What: Verify that a file path is not identified as a package.
    Why: Ensure the method only accepts directories.
    """
    file_path = tmp_path / "not_a_dir.py"
    file_path.touch()
    
    assert SourceCrawler.is_package(file_path) is False

# end of file test/02_01_02_crawler_sourcecrawler_is_package_test.py
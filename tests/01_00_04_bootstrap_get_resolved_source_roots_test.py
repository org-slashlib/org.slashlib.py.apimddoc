# -*- coding: utf-8 -*-
# file test/01_00_04_bootstrap_get_resolved_source_roots_test.py
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
Module: bootstrap.py
Class: N/A (Standalone function)
Function: get_resolved_source_roots

Special Considerations:
- This test suite ensures that relative source roots are correctly resolved 
  into absolute POSIX path strings based on the location of pyproject.toml.
- Dependencies: Requires functional get_pyproject_path and get_source_roots.
"""

import pytest
import pathlib
from org.slashlib.py.apimddoc.bootstrap import get_resolved_source_roots

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the function is importable and callable before running logic tests.
    """
    assert callable(get_resolved_source_roots), "get_resolved_source_roots must be a function"

def test_get_resolved_source_roots_success(monkeypatch, tmp_path):
    """
    What: Verify that relative paths are resolved to absolute POSIX paths.
    Why: To ensure that the project root is correctly identified and prepended 
         to the source directories.
    """
    # 1. Setup: Create a dummy pyproject.toml
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text("")
    
    # 2. Mock: get_pyproject_path to return our temp file
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_pyproject_path", lambda: pyproject)
    
    # 3. Mock: get_source_roots to return a relative path
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_source_roots", lambda: ("src",))
    
    # 4. Execute
    result = get_resolved_source_roots()
    
    # 5. Assert: The path should be absolute
    expected_path = (tmp_path / "src").resolve()
    assert result == (expected_path,)

def test_get_resolved_source_roots_multiple(monkeypatch, tmp_path):
    """
    What: Verify resolution for multiple source roots.
    Why: Ensure the function handles multiple entries consistently.
    """
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text("")
    
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_pyproject_path", lambda: pyproject)
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_source_roots", lambda: ("src1", "src2"))
    
    result = get_resolved_source_roots()
    
    expected1 = (tmp_path / "src1").resolve()
    expected2 = (tmp_path / "src2").resolve()
    
    assert result == (expected1, expected2)

# end of file test/01_00_04_bootstrap_get_resolved_source_roots_test.py
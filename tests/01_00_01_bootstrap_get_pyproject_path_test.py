# -*- coding: utf-8 -*-
# file test/01_00_01_bootstrap_get_pyproject_path_test.py
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
Function: get_pyproject_path
Special Considerations: The test verifies correct path resolution and error 
handling when the file is absent.
"""

import pytest
import pathlib
from org.slashlib.py.apimddoc.bootstrap import get_pyproject_path

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the function is importable and callable before running logic tests.
    """
    assert callable(get_pyproject_path), "get_pyproject_path must be a function"

def test_get_pyproject_path_file_not_found(monkeypatch, tmp_path):
    """
    What: Test behavior when pyproject.toml is missing.
    Why: Ensure that a FileNotFoundError is raised as expected.
    """
    monkeypatch.setattr(pathlib.Path, "cwd", lambda: tmp_path)
    
    with pytest.raises(FileNotFoundError, match="Could not find pyproject.toml"):
        get_pyproject_path()

def test_get_pyproject_path_success(monkeypatch, tmp_path):
    """
    What: Test behavior when pyproject.toml exists.
    Why: Verify that the function returns the correct absolute path.
    """
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text("")
    
    monkeypatch.setattr(pathlib.Path, "cwd", lambda: tmp_path)
    
    result = get_pyproject_path()
    assert result == pyproject.resolve()

# end of file test/01_00_01_bootstrap_get_pyproject_path_test.py
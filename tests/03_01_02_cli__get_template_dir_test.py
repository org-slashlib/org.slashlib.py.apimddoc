# -*- coding: utf-8 -*-
# file test/03_01_02_cli__get_template_dir_test.py
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
Module: cli.py
Class: N/A (Standalone function)
Function: _get_template_dir
Special Considerations: 
- Verifies the resolution logic including the fallback mechanism to package resources.
"""

import pytest
import pathlib
import importlib.resources
from org.slashlib.py.apimddoc.cli import _get_template_dir

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the function is importable and callable.
    """
    assert callable(_get_template_dir), "_get_template_dir must be a function"

def test_get_template_dir_found(tmp_path, monkeypatch):
    """
    What: Verify that the found path is returned when templates exist.
    Why: Ensure the function respects the result of _find_template_dir.
    """
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    
    # Mock _find_template_dir to return our dummy dir
    monkeypatch.setattr("org.slashlib.py.apimddoc.cli._find_template_dir", lambda x: template_dir)
    
    result = _get_template_dir(("some/root",))
    assert result == template_dir

def test_get_template_dir_fallback_when_none(monkeypatch):
    """
    What: Verify fallback to package resources when _find_template_dir returns None.
    Why: Ensure the system remains functional even if no local templates are found.
    """
    # Mock _find_template_dir to return None
    monkeypatch.setattr("org.slashlib.py.apimddoc.cli._find_template_dir", lambda x: None)
    
    # We expect the fallback path from importlib.resources
    result = _get_template_dir(("some/root",))
    
    assert result is not None
    assert result.name == "templates"

def test_get_template_dir_fallback_on_exception(monkeypatch):
    """
    What: Verify fallback when _find_template_dir raises an exception.
    Why: Ensure robust error handling for unexpected runtime issues.
    """
    # Mock _find_template_dir to raise an error
    monkeypatch.setattr("org.slashlib.py.apimddoc.cli._find_template_dir", lambda x: exec("raise ValueError('Boom')"))
    
    # Should fall back to package resources without crashing
    result = _get_template_dir(("some/root",))
    assert result is not None

# end of file test/03_01_02_cli__get_template_dir_test.py
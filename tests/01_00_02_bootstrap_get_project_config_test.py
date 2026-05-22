# -*- coding: utf-8 -*-
# file test/01_00_02_bootstrap_get_project_config_test.py
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
Function: get_project_config

Special Considerations:
- This test suite ensures source root resolution is strictly based on pyproject.toml.
- The test must handle the absence of a pyproject.toml gracefully and verify behavior
  when the file exists in the CWD.
- Design Decisions regarding ignored scenarios:
    1. External Project Paths (e.g., ['../outside_root']): Ignored. 
       The tool does not validate external path security; it trusts the config.
    2. System/Dependency State: Ignored. 
       The environment setup is the responsibility of the host, not the tool.       
    3. Multiple 'where' entries: Supported. The function returns a tuple of all 
       resolved paths found in the configuration.
    4. Missing Configuration: Handled as a critical failure (ValueError). 
       Implicit defaults are explicitly disabled to prevent misconfiguration.
    5. Path Validation: The tool expects the configured paths to exist.
"""

import pytest
import pathlib
from org.slashlib.py.apimddoc.bootstrap import get_project_config

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the function is importable and callable before running logic tests.
    """
    assert callable(get_project_config), "get_project_config must be a function"

def test_get_project_config_file_not_found(monkeypatch, tmp_path):
    """
    What: Test behavior when pyproject.toml is missing.
    Why: Ensure the function raises FileNotFoundError as per current implementation.
    """
    # Mock Path.cwd to point to an empty directory
    monkeypatch.setattr(pathlib.Path, "cwd", lambda: tmp_path)
    
    # Assert that FileNotFoundError is raised when pyproject.toml is missing
    with pytest.raises(FileNotFoundError):
        get_project_config()

def test_get_project_config_success(tmp_path, monkeypatch):
    """
    What: Test behavior when pyproject.toml exists.
    Why: Verify that the TOML content is correctly parsed and returned.
    Assumptions: A valid pyproject.toml file is present in the working directory.
    """
    # Create a temporary pyproject.toml
    d = tmp_path
    p = d / "pyproject.toml"
    p.write_text("[project]\nname = 'test-project'")
    
    # Mock Path.cwd to point to temporary directory
    monkeypatch.setattr(pathlib.Path, "cwd", lambda: d)
    
    result = get_project_config()
    assert result["project"]["name"] == "test-project"

# end of file test/01_00_02_bootstrap_get_project_config_test.py
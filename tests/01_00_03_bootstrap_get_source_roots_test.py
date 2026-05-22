# -*- coding: utf-8 -*-
# file test/01_00_03_bootstrap_get_source_roots_test.py
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
Function: get_source_roots

Special Considerations:
- This test suite ensures source root resolution is strictly based on pyproject.toml.
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
from org.slashlib.py.apimddoc.bootstrap import get_source_roots

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the function is importable and callable before running logic tests.
    """
    assert callable(get_source_roots), "get_source_roots must be a function"

def test_get_source_roots_no_config_failure(monkeypatch):
    """
    What: Verify that the absence of configuration leads to a ValueError.
    Why: The tool requires an explicit configuration to determine the source root.
    """
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_project_config", lambda: {})
    
    with pytest.raises(ValueError, match="Missing"):
        get_source_roots()

def test_get_source_roots_with_config(monkeypatch, tmp_path):
    """
    What: Verify source root resolution based on pyproject.toml configuration.
    Why: Ensure that if 'where' is configured, the function resolves the path 
         correctly relative to the location of pyproject.toml (CWD).
    """
    mock_config = {
        "tool": {
            "setuptools": {
                "packages": {
                    "find": {"where": ["custom_src"]}
                }
            }
        }
    }
    
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_project_config", lambda: mock_config)
    
    # Assert result matches the string returned by the current implementation
    result = get_source_roots()
    assert result == ("custom_src",)

def test_get_source_roots_multiple_paths(monkeypatch, tmp_path):
    """
    What: Verify that multiple source paths defined in pyproject.toml are correctly resolved.
    Why: To ensure the tool can handle complex project structures with multiple source directories.
    """
    mock_config = {
        "tool": {
            "setuptools": {
                "packages": {
                    "find": {"where": ["src1", "src2"]}
                }
            }
        }
    }
    
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_project_config", lambda: mock_config)
    
    # Assert result matches the tuple of strings returned by the current implementation
    result = get_source_roots()
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result == ("src1", "src2")

def test_get_source_roots_single_string_config(monkeypatch):
    """
    What: Verify that a single string entry in 'where' is correctly handled.
    Why: To ensure the function handles both list and string inputs for the 
         'where' configuration gracefully.
    """
    # Mock config where 'where' is a single string
    mock_config = {
        "tool": {
            "setuptools": {
                "packages": {
                    "find": {"where": "src"}
                }
            }
        }
    }
    
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_project_config", lambda: mock_config)
    
    # Assert result handles the single string correctly and returns a tuple
    result = get_source_roots()
    assert result == ("src",)

# end of file test/01_00_03_bootstrap_get_source_roots_test.py
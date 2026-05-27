# -*- coding: utf-8 -*-
# file test/01_00_05_bootstrap_get_document_output_dir_test.py
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
Function: get_document_output_dir

Special Considerations:
- This test suite ensures that the output directory resolution follows the order:
  1. Provided argument.
  2. Configuration loader (via configloader).
  3. Fallback to project_root/docs.
"""

import pytest
import pathlib
from unittest.mock import patch, MagicMock
from org.slashlib.py.apimddoc.bootstrap import get_document_output_dir

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the function is importable and callable.
    """
    assert callable(get_document_output_dir), "get_document_output_dir must be a function"

def test_get_document_output_dir_explicit_path(tmp_path):
    """
    What: Verify that an explicitly provided path is used.
    Why: The argument should always take precedence over configuration or defaults.
    """
    custom_path = tmp_path / "custom_docs"
    result = get_document_output_dir(str(custom_path))
    
    assert result == custom_path
    assert result.exists()

@patch("org.slashlib.py.configloader.resolve")
def test_get_document_output_dir_from_config(mock_resolve, tmp_path):
    """
    What: Verify that the path is resolved via configloader when no argument is provided.
    Why: Ensure standard configuration-based output paths are respected.
    """
    config_path = tmp_path / "config_docs"
    mock_resolve.return_value = str(config_path)
    
    result = get_document_output_dir()
    
    assert result == config_path
    mock_resolve.assert_called_with("paths.api", default=None)

@patch("org.slashlib.py.configloader.resolve")
@patch("org.slashlib.py.apimddoc.bootstrap.get_pyproject_path")
def test_get_document_output_dir_fallback(mock_get_path, mock_resolve, tmp_path):
    """
    What: Verify fallback to project_root/docs when no argument or config is provided.
    Why: Ensure a sensible default exists for unconfigured projects.
    """
    # Setup mock
    pyproject = tmp_path / "pyproject.toml"
    pyproject.touch()
    mock_get_path.return_value = pyproject
    mock_resolve.return_value = None
    
    expected_default = tmp_path / "docs"
    
    result = get_document_output_dir()
    
    assert result == expected_default
    assert result.exists()

# end of file test/01_00_05_bootstrap_get_document_output_dir_test.py
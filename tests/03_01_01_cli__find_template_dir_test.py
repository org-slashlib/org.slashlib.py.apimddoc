# -*- coding: utf-8 -*-
# file test/03_01_01_cli__find_template_dir_test.py
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
Function: _find_template_dir
Special Considerations: 
- Tests path resolution logic for template directories relative to source roots.
- Verifies behavior when the directory exists versus when it does not.
"""

import pytest
import pathlib
from org.slashlib.py.apimddoc.cli import _find_template_dir

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the function is importable and callable before running logic tests.
    """
    assert callable(_find_template_dir), "_find_template_dir must be a function"

def test_find_template_dir_found(tmp_path):
    """
    What: Verify that the function locates the template directory when it exists.
    Why: Ensure correct parent navigation logic (source_root.parent.parent / "templates").
    """
    # Structure: tmp_path / project_root / src / custom_src
    # Expected templates path: tmp_path / project_root / templates
    project_root = tmp_path / "project"
    source_src = project_root / "src" / "custom_src"
    source_src.mkdir(parents=True)
    
    template_dir = project_root / "templates"
    template_dir.mkdir()
    
    resolved_roots = (str(source_src),)
    
    result = _find_template_dir(resolved_roots)
    assert result == template_dir

def test_find_template_dir_not_found(tmp_path):
    """
    What: Verify that the function returns None when the template directory does not exist.
    Why: To ensure fallback mechanisms in higher-level functions are triggered correctly.
    """
    source_src = tmp_path / "src"
    source_src.mkdir()
    
    resolved_roots = (str(source_src),)
    
    result = _find_template_dir(resolved_roots)
    assert result is None

def test_find_template_dir_found_in_root(tmp_path):
    """
    What: Verify templates are found when located at source_root.parent.parent / "templates".
    Why: The implementation logic strictly relies on this specific directory hierarchy.
    """
    # Create structure: base/project/src
    project_dir = tmp_path / "project"
    source_dir = project_dir / "src"
    source_dir.mkdir(parents=True)
    
    # Create templates at base/templates (which is source_dir.parent.parent)
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    
    result = _find_template_dir((str(source_dir),))
    assert result == template_dir

def test_find_template_dir_multiple_roots_first_fails_second_succeeds(tmp_path):
    """
    What: Verify that the function iterates through roots and stops at the first match.
    Why: Ensure logic correctly continues searching when the first root lacks templates.
    """
    # Root 1 (No templates)
    root1 = tmp_path / "root1" / "src"
    root1.mkdir(parents=True)
    
    # Root 2 (With templates)
    # The function expects templates at root2.parent.parent / "templates"
    # Which is tmp_path / "templates"
    root2 = tmp_path / "root2" / "src"
    root2.mkdir(parents=True)
    
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    
    result = _find_template_dir((str(root1), str(root2)))
    assert result == template_dir

def test_find_template_dir_none_found(tmp_path):
    """
    What: Verify returns None when no templates exist in any parent.parent hierarchy.
    Why: Ensure graceful handling of missing template directories.
    """
    source_dir = tmp_path / "isolated" / "src"
    source_dir.mkdir(parents=True)
    
    result = _find_template_dir((str(source_dir),))
    assert result is None

# end of file test/03_01_01_cli__find_template_dir_test.py
# -*- coding: utf-8 -*-
# file test/31_01_04_markdownrenderer__get_template_test.py
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

import pytest
from unittest.mock import MagicMock
from jinja2 import Template
from org.slashlib.py.apimddoc.renderer.markdown import MarkdownRenderer

def test_markdownrenderer__get_template_exists():
    """
    What: Verify existence of _get_template.
    Why: Integrity check of the test object.
    """
    assert hasattr(MarkdownRenderer, "_get_template")

def test_markdownrenderer__get_template_loads():
    """
    What: Verify that _get_template loads and returns a template.
    Why: Ensure template retrieval works correctly via the environment.
    """
    # Mocking the internal environment
    mock_env = MagicMock()
    mock_template = MagicMock(spec=Template)
    mock_env.get_template.return_value = mock_template
    MarkdownRenderer._env = mock_env
    
    template_name = "test.md.j2"
    result = MarkdownRenderer._get_template(template_name)
    
    assert result == mock_template
    mock_env.get_template.assert_called_once_with(template_name)

# end of file test/31_01_04_markdownrenderer__get_template_test.py
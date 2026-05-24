# -*- coding: utf-8 -*-
# file test/31_01_03_markdownrenderer_setup_test.py
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
import jinja2
from org.slashlib.py.apimddoc.renderer.markdown import MarkdownRenderer

def test_markdownrenderer_setup_exists():
    """
    What: Verify existence of setup.
    Why: Integrity check of the test object.
    """
    assert hasattr(MarkdownRenderer, "setup")

def test_markdownrenderer_setup_configures_env():
    """
    What: Verify that setup configures the jinja2 environment.
    Why: Ensure the renderer is ready for template loading after setup.
    """
    template_dir = "tests/fixtures/templates"
    MarkdownRenderer.setup(template_dir)
    
    assert isinstance(MarkdownRenderer._env, jinja2.Environment)
    assert isinstance(MarkdownRenderer._env.loader, jinja2.FileSystemLoader)

# end of file test/31_01_03_markdownrenderer_setup_test.py
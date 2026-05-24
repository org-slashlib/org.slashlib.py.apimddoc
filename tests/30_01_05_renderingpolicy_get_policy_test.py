# -*- coding: utf-8 -*-
# file test/30_01_05_renderingpolicy_get_policy_test.py
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
from unittest.mock import patch, MagicMock
from org.slashlib.py.apimddoc.renderer.policy import RenderingPolicy

def test_renderingpolicy_get_policy_exists():
    """
    What: Verify existence of get_policy.
    Why: Integrity check of the test object.
    """
    assert hasattr(RenderingPolicy, "get_policy")

def test_renderingpolicy_get_policy_default():
    """
    What: Verify default policy return.
    Why: Ensure it returns itself when no plugin is registered.
    """
    with patch("importlib.metadata.entry_points", return_value=[]):
        policy = RenderingPolicy.get_policy()
        assert policy is RenderingPolicy

def test_renderingpolicy_get_policy_custom_plugin():
    """
    What: Verify custom plugin loading.
    Why: Ensure it loads and returns the custom policy class from entry points.
    """
    mock_ep = MagicMock()
    mock_policy_class = type("CustomPolicy", (RenderingPolicy,), {})
    mock_ep.load.return_value = mock_policy_class
    
    with patch("importlib.metadata.entry_points", return_value=[mock_ep]):
        policy = RenderingPolicy.get_policy()
        assert policy is mock_policy_class

# end of file test/30_01_05_renderingpolicy_get_policy_test.py
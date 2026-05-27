# -*- coding: utf-8 -*-
# file test/31_01_05_markdownrenderer_render_test.py
# @AI:
# - INTEGRITY RULES:
#   - STRICT PRESERVATION: Do not remove, move, or modify ANY existing lines of code or comments 
#     unless they are the explicit target of the requested change. 
#   - DEBUG MARKERS: Commented-out code (e.g., debug prints) MUST be kept exactly where they are.
#   - WHITESPACE & STRUCTURE: Maintain all original empty lines and the existing file structure. 
#     Structural integrity takes precedence over "clean code" or "elegance".
#   - LEAD-IN/OUT: The very first and last lines (and all comments in between) are immutable anchors.
# - MAINTENANCE:
#   - Only update pydoc strings (args, returns, expires) if the function signature changes.
#   - Do NOT delete existing examples or descriptions in pydoc.
# - LANGUAGE: en-US for all comments and documentation.
#

import pytest
from unittest.mock import patch, MagicMock
from org.slashlib.py.apimddoc.renderer.markdown import MarkdownRenderer

def test_markdownrenderer_render_exists():
    """
    What: Verify existence of render.
    Why: Integrity check of the test object.
    """
    assert hasattr(MarkdownRenderer, "render")

def test_markdownrenderer_render_unconfigured_raises():
    """
    What: Verify that render raises RuntimeError if not configured.
    Why: Ensure safety check for uninitialized environment.
    """
    MarkdownRenderer._env = None
    with pytest.raises(RuntimeError, match="MarkdownRenderer not configured"):
        MarkdownRenderer.render("output")

@patch("org.slashlib.py.apimddoc.core.registry.ProjectRegistry")
@patch("org.slashlib.py.apimddoc.renderer.markdown.RenderingPolicy.get_policy")
@patch("org.slashlib.py.apimddoc.renderer.markdown.pathlib.Path")
def test_markdownrenderer_render_success(mock_path_cls, mock_get_policy, mock_registry_cls):
    """
    What: Verify successful rendering execution.
    Why: Ensure templates are loaded and files are written when registry is populated.
    """
    # Setup mocks
    mock_env = MagicMock()
    mock_template = MagicMock()
    mock_template.render.return_value = "rendered content"
    mock_env.get_template.return_value = mock_template
    MarkdownRenderer._env = mock_env
    
    # Setup registry mock
    mock_registry = mock_registry_cls
    mock_registry.list_all_modules.return_value = [MagicMock()]
    
    mock_policy = MagicMock()
    mock_policy.should_render_entity.return_value = True
    mock_policy.get_template_name.return_value = "test.j2"
    mock_policy.get_markdown_filename.return_value = "test.md"
    mock_get_policy.return_value = mock_policy
    
    # Setup path mock chain
    mock_path_instance = MagicMock()
    mock_path_cls.return_value = mock_path_instance
    # Allow chained calls like output_path / filename and target_file.parent
    mock_path_instance.__truediv__.return_value = mock_path_instance
    mock_path_instance.parent = mock_path_instance
    
    # Execute
    MarkdownRenderer.render("output")
    
    # Assert
    mock_path_instance.write_text.assert_called_once_with("rendered content", encoding="utf-8")
    mock_env.get_template.assert_called_with("test.j2")

# end of file test/31_01_05_markdownrenderer_render_test.py
# -*- coding: utf-8 -*-
# file test/30_01_04_renderingpolicy_get_markdown_filename_test.py
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
from org.slashlib.py.apimddoc.renderer.policy import RenderingPolicy
from org.slashlib.py.apimddoc.core.models import (
    ModuleModel, ClassModel, FunctionModel, BaseModel
)

def test_renderingpolicy_get_markdown_filename_exists():
    """
    What: Verify existence of get_markdown_filename.
    Why: Integrity check of the test object.
    """
    assert hasattr(RenderingPolicy, "get_markdown_filename")

def test_renderingpolicy_get_markdown_filename_module():
    """
    What: Test ModuleModel filename generation.
    Why: Verify module models map to {fqmn}.md.
    """
    model = ModuleModel(name="m", fqmn="m", file_path="m.py", display_namespace="n", source_namespace="n")
    assert RenderingPolicy.get_markdown_filename(model) == "m.md"

def test_renderingpolicy_get_markdown_filename_class():
    """
    What: Test ClassModel filename generation.
    Why: Verify class models map to {fqmn}.{name}.md.
    """
    model = ClassModel(name="C", fqmn="m", file_path="C.py", canonical_path="C", display_namespace="n", source_namespace="n")
    assert RenderingPolicy.get_markdown_filename(model) == "m.C.md"

def test_renderingpolicy_get_markdown_filename_function():
    """
    What: Test FunctionModel filename generation.
    Why: Verify function models map to {fqmn}.{name}.md.
    """
    model = FunctionModel(name="f", fqmn="m", file_path="f.py", source_namespace="n", display_namespace="n")
    assert RenderingPolicy.get_markdown_filename(model) == "m.f.md"

def test_renderingpolicy_get_markdown_filename_invalid_model():
    """
    What: Test invalid model raises ValueError.
    Why: Ensure robust error handling for unknown model types.
    """
    class UnknownModel(BaseModel):
        pass
    model = UnknownModel(name="u", fqmn="u", file_path="u.py")
    with pytest.raises(ValueError, match="No filename pattern defined for model type"):
        RenderingPolicy.get_markdown_filename(model)

# end of file test/30_01_04_renderingpolicy_get_markdown_filename_test.py
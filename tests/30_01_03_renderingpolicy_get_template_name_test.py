# -*- coding: utf-8 -*-
# file test/30_01_03_renderingpolicy_get_template_name_test.py
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

def test_renderingpolicy_get_template_name_exists():
    """
    What: Verify existence of get_template_name.
    Why: Integrity check of the test object.
    """
    assert hasattr(RenderingPolicy, "get_template_name")

def test_renderingpolicy_get_template_name_module():
    """
    What: Test ModuleModel mapping.
    Why: Verify correct template mapping for module models.
    """
    model = ModuleModel(name="m", fqmn="m", file_path="m.py", display_namespace="n", source_namespace="n")
    assert RenderingPolicy.get_template_name(model) == "module.md.j2"

def test_renderingpolicy_get_template_name_class():
    """
    What: Test ClassModel mapping.
    Why: Verify correct template mapping for class models.
    """
    model = ClassModel(name="C", fqmn="C", file_path="C.py", canonical_path="C", display_namespace="n", source_namespace="n")
    assert RenderingPolicy.get_template_name(model) == "class.md.j2"

def test_renderingpolicy_get_template_name_function():
    """
    What: Test FunctionModel mapping.
    Why: Verify correct template mapping for function models.
    """
    model = FunctionModel(name="f", fqmn="f", file_path="f.py", source_namespace="n", display_namespace="n")
    assert RenderingPolicy.get_template_name(model) == "function.md.j2"

def test_renderingpolicy_get_template_name_invalid_model():
    """
    What: Test invalid model raises ValueError.
    Why: Ensure robust error handling for unknown model types.
    """
    class UnknownModel(BaseModel):
        pass
    # Pass all three required arguments to satisfy BaseModel.__init__
    model = UnknownModel(name="u", fqmn="u", file_path="u.py")
    with pytest.raises(ValueError, match="No template mapped for model type"):
        RenderingPolicy.get_template_name(model)

# end of file test/30_01_03_renderingpolicy_get_template_name_test.py
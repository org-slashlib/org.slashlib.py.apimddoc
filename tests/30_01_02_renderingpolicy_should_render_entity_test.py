# -*- coding: utf-8 -*-
# file test/30_01_02_renderingpolicy_should_render_entity_test.py
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
import pathlib
from org.slashlib.py.apimddoc.renderer.policy import RenderingPolicy
from org.slashlib.py.apimddoc.core.models import (
    NamespaceModuleModel, ModuleModel, ClassModel, FunctionModel
)

def test_renderingpolicy_should_render_entity_exists():
    """
    What: Verify existence of should_render_entity.
    Why: Integrity check of the test object.
    """
    assert hasattr(RenderingPolicy, "should_render_entity")

def test_renderingpolicy_should_render_entity_namespace_module():
    """
    What: Test NamespaceModuleModel returns False.
    Why: Namespace modules should not be rendered.
    """
    ns_model = NamespaceModuleModel(
        name="test", 
        fqmn="test", 
        file_path=pathlib.Path("test.py"), 
        display_namespace="n", 
        source_namespace="n"
    )
    assert RenderingPolicy.should_render_entity(ns_model) is False

def test_renderingpolicy_should_render_entity_empty_module():
    """
    What: Test empty ModuleModel returns False.
    Why: Modules without content should not be rendered.
    """
    empty_mod = ModuleModel(name="m", fqmn="m", file_path=None, display_namespace="n", source_namespace="n")
    assert RenderingPolicy.should_render_entity(empty_mod) is False

def test_renderingpolicy_should_render_entity_filled_module():
    """
    What: Test ModuleModel with exported names returns True.
    Why: Modules with content should be rendered.
    """
    filled_mod = ModuleModel(name="m", fqmn="m", file_path=None, display_namespace="n", source_namespace="n")
    # exported_names is a set, use add()
    filled_mod.exported_names.add("test_name")
    assert RenderingPolicy.should_render_entity(filled_mod) is True

def test_renderingpolicy_should_render_entity_class():
    """
    What: Test ClassModel returns True.
    Why: Class entities should be rendered.
    """
    class_model = ClassModel(name="C", fqmn="C", file_path=None, canonical_path="C", display_namespace="n", source_namespace="n")
    assert RenderingPolicy.should_render_entity(class_model) is True

def test_renderingpolicy_should_render_entity_function():
    """
    What: Test FunctionModel returns True.
    Why: Function entities should be rendered.
    """
    func_model = FunctionModel(name="f", fqmn="f", file_path=None, display_namespace="n", source_namespace="n")
    assert RenderingPolicy.should_render_entity(func_model) is True

# end of file test/30_01_02_renderingpolicy_should_render_entity_test.py
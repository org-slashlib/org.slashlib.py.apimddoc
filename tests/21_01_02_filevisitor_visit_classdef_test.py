# -*- coding: utf-8 -*-
# file test/21_01_02_filevisitor_visit_classdef_test.py
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

import ast
import pathlib
import pytest
from org.slashlib.py.apimddoc.parser.filevisitor import FileVisitor
from org.slashlib.py.apimddoc.core.models.modulemodel import ModuleModel

def test_filevisitor_visit_classdef():
    """
    What: Test the visit_ClassDef method of FileVisitor.
    Why: Verify that a ClassModel is created and added to the ModuleModel when visiting a ClassDef node.
    """
    # Setup ModuleModel
    module_model = ModuleModel(
        name="test_mod",
        fqmn="test_mod",
        file_path=pathlib.Path("test.py"),
        display_namespace="test",
        source_namespace="test"
    )
    visitor = FileVisitor(module_model)
    
    # Create an AST ClassDef node
    class_node = ast.ClassDef(
        name="TestClass",
        bases=[],
        keywords=[],
        body=[],
        decorator_list=[]
    )
    
    # Execute visitor
    visitor.visit_ClassDef(class_node)
    
    # Verify results   
    assert len(module_model.classes) == 1
    class_model = module_model.classes["TestClass"]
    assert class_model.name == "TestClass"    
    assert class_model.fqmn == "test_mod.TestClass"
# -*- coding: utf-8 -*-
# file test/21_01_03_filevisitor_visit_functiondef_test.py
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
from org.slashlib.py.apimddoc.core.models.classmodel import ClassModel


def test_filevisitor_visit_functiondef():
    """
    What: Test the visit_FunctionDef method of FileVisitor for a standalone function.
    Why: Verify that a FunctionModel is created and added to the ModuleModel.
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
    
    # Create an AST FunctionDef node
    func_node = ast.FunctionDef(
        name="test_function",
        args=ast.arguments(
            args=[], vararg=None, kwonlyargs=[], kw_defaults=[], defaults=[]
        ),
        body=[],
        decorator_list=[]
    )
    
    # Execute visitor
    visitor.visit_FunctionDef(func_node)
    
    # Verify results (assuming module_model.functions is a dict or list based on previous findings)
    # Adjust accessing depending on ModuleModel implementation (e.g., list(module_model.functions.values()))
    functions = list(module_model.functions.values()) if isinstance(module_model.functions, dict) else module_model.functions
    assert len(functions) == 1
    assert functions[0].name == "test_function"
    
def test_filevisitor_visit_methoddef():
    """
    What: Test the visit_FunctionDef method of FileVisitor for a class method.
    Why: Verify that a FunctionModel is added to the current ClassModel.
    """
    # Setup
    module_model = ModuleModel(
        name="test_mod",
        fqmn="test_mod",
        file_path=pathlib.Path("test.py"),
        display_namespace="test",
        source_namespace="test"
    )
    visitor = FileVisitor(module_model)
    
    # Create and set current_class state
    class_model = ClassModel(
        name="TestClass",
        fqmn="test_mod.TestClass",
        file_path=pathlib.Path("test.py"),
        canonical_path="test_mod.TestClass",
        display_namespace="test",
        source_namespace="test"
    )
    visitor.current_class = class_model
    
    # Create AST FunctionDef node
    func_node = ast.FunctionDef(
        name="test_method",
        args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], defaults=[]),
        body=[],
        decorator_list=[]
    )
    
    # Execute visitor
    visitor.visit_FunctionDef(func_node)
    
    # Verify results
    # Access methods based on your ClassModel implementation (likely .methods)
    methods = list(class_model.methods.values()) if isinstance(class_model.methods, dict) else class_model.methods
    assert len(methods) == 1
    assert methods[0].name == "test_method"    
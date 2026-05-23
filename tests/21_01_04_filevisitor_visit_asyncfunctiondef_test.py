# -*- coding: utf-8 -*-
# file test/21_01_04_filevisitor_visit_asyncfunctiondef_test.py
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

def test_filevisitor_visit_asyncfunctiondef():
    """
    What: Test the visit_AsyncFunctionDef method of FileVisitor.
    Why: Verify that an AsyncFunctionDef node is processed identically to a FunctionDef node.
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
    
    # Create an AST AsyncFunctionDef node
    async_func_node = ast.AsyncFunctionDef(
        name="test_async_function",
        args=ast.arguments(
            args=[], vararg=None, kwonlyargs=[], kw_defaults=[], defaults=[]
        ),
        body=[],
        decorator_list=[]
    )
    
    # Execute visitor
    visitor.visit_AsyncFunctionDef(async_func_node)
    
    # Verify results
    functions = list(module_model.functions.values()) if isinstance(module_model.functions, dict) else module_model.functions
    assert len(functions) == 1
    assert functions[0].name == "test_async_function"

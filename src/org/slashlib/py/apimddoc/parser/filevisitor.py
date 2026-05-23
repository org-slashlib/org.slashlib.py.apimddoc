# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/parser/filevisitor.py
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
import typing

from org.slashlib.py.apimddoc.core.models.modulemodel import ModuleModel
from org.slashlib.py.apimddoc.core.models.classmodel import ClassModel
from org.slashlib.py.apimddoc.core.models.functionmodel import FunctionModel


class FileVisitor(ast.NodeVisitor):
    """
    AST Visitor to traverse a Python file and extract classes and functions.
    
    This visitor populates the provided ModuleModel with ClassModel and 
    FunctionModel instances found during the AST traversal.
    """

    def __init__(self, module_model: ModuleModel):
        """
        Initializes the FileVisitor with a target ModuleModel.

        Args:
            module_model (ModuleModel): The module model to populate.
        """
        self.module_model = module_model
        self.current_class: typing.Optional[ClassModel] = None

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """
        Visits a class definition node and creates a ClassModel.

        Args:
            node (ast.ClassDef): The AST node representing the class.
        """
        # Create a new ClassModel
        class_model = ClassModel(
            name=node.name,
            fqmn=f"{self.module_model.fqmn}.{node.name}",
            file_path=self.module_model.file_path,
            canonical_path=f"{self.module_model.fqmn}.{node.name}",
            display_namespace=self.module_model.display_namespace,
            source_namespace=self.module_model.source_namespace
        )
        class_model.docstring = ast.get_docstring(node)
        
        # Track state and add to module
        parent_class = self.current_class
        self.current_class = class_model
        self.module_model.add_class(class_model)
        
        # Traverse children
        self.generic_visit(node)
        
        # Restore state
        self.current_class = parent_class

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """
        Visits a function/method definition node.

        Args:
            node (ast.FunctionDef): The AST node representing the function/method.
        """
        # Create a new FunctionModel
        function_model = FunctionModel(
            name=node.name,
            fqmn=f"{self.module_model.fqmn}.{node.name}",
            file_path=self.module_model.file_path,
            source_namespace=self.module_model.source_namespace,
            display_namespace=self.module_model.display_namespace
        )
        function_model.docstring = ast.get_docstring(node)
        
        # Decide if this is a method of a class or a standalone function
        if self.current_class:
            self.current_class.add_method(function_model)
        else:
            self.module_model.add_function(function_model)
            
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """
        Visits an async function definition node. Treated same as FunctionDef.

        Args:
            node (ast.AsyncFunctionDef): The AST node representing the async function.
        """
        self.visit_FunctionDef(node)


# end of file src/org/slashlib/py/apimddoc/parser/filevisitor.py
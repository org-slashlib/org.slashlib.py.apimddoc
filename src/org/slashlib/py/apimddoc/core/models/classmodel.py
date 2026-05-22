# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/core/models/classmodel.py
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

# python imports
import typing

# internal imports
from org.slashlib.py.apimddoc.core.models.basemodel import BaseModel
from org.slashlib.py.apimddoc.core.models.functionmodel import FunctionModel
from org.slashlib.py.apimddoc.core.models.propertymodel import PropertyModel

class ClassModel(BaseModel):
    """
    Represents a parsed class with its metadata.

    Extends BaseModel to include specific attributes for class documentation,
    namespaces, docstrings, public status, and lists of methods and properties.

    Args:
        name (str): The name of the entity.
        fqmn (str): The Fully Qualified Module Name.
        file_path (str): The file path where the entity is defined.
        canonical_path (str): The canonical path of the class.
        display_namespace (str): The human-readable namespace for display.
        source_namespace (str): The actual source code namespace.
    """

    def __init__(
        self, 
        name: str, 
        fqmn: str, 
        file_path: str, 
        canonical_path: str, 
        display_namespace: str, 
        source_namespace: str
    ):
        """Initializes the ClassModel instance."""
        super().__init__(name, fqmn, file_path)
        
        self.canonical_path = canonical_path
        self.display_namespace = display_namespace
        self.source_namespace = source_namespace
        self.docstring: typing.Optional[str] = None
        self.is_public: bool = False
        self.methods: typing.List[FunctionModel] = []
        self.properties: typing.List[PropertyModel] = []

    def add_method(self, method: FunctionModel) -> None:
        """
        Adds a method to the class.

        Args:
            method (FunctionModel): The method to be added.
        """
        self.methods.append(method)

    def add_property(self, prop: PropertyModel) -> None:
        """
        Adds a property to the class.

        Args:
            prop (PropertyModel): The property to be added.
        """
        self.properties.append(prop)

# end of file src/org/slashlib/py/apimddoc/core/models/classmodel.py
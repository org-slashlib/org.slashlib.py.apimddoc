# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/core/models/basemodulemodel.py
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

class BaseModuleModel(BaseModel):
    """
    Base class for all module types.

    Extends BaseModel to include specific attributes for module documentation,
    such as display and source namespaces, associated docstrings, and children.
    """

    def __init__(self, name: str, fqmn: str, file_path: str, display_namespace: str, source_namespace: str):
        """
        Initializes the BaseModuleModel instance.

        Args:
            name (str): The name of the entity.
            fqmn (str): The Fully Qualified Module Name.
            file_path (str): The file path where the entity is defined.
            display_namespace (str): The human-readable namespace for display.
            source_namespace (str): The actual source code namespace.
        """
        super().__init__(name, fqmn, file_path)
        
        self.display_namespace = display_namespace
        self.source_namespace = source_namespace
        self.docstring: typing.Optional[str] = None
        self.submodules: typing.List['BaseModuleModel'] = []

    def add_submodule(self, submodule: 'BaseModuleModel') -> None:
        """
        Adds a submodule to the current module.

        Args:
            submodule (BaseModuleModel): The module to be added as a child.
        """
        self.submodules.append(submodule)

# end of file src/org/slashlib/py/apimddoc/core/models/basemodulemodel.py
# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/core/models/modulemodel.py
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
from org.slashlib.py.apimddoc.core.models.basemodulemodel import BaseModuleModel
from org.slashlib.py.apimddoc.core.models.classmodel import ClassModel
from org.slashlib.py.apimddoc.core.models.functionmodel import FunctionModel

class ModuleModel(BaseModuleModel):
    """
    Represents a standard package or module (has __init__.py or is .py file).

    Extends BaseModuleModel to include collections of classes, functions,
    and a set of exported names.

    Args:
        name (str): The name of the entity.
        fqmn (str): The Fully Qualified Module Name.
        file_path (str): The file path where the entity is defined.
        display_namespace (str): The human-readable namespace for display.
        source_namespace (str): The actual source code namespace.
    """

    def __init__(
        self, 
        name: str, 
        fqmn: str, 
        file_path: str, 
        display_namespace: str, 
        source_namespace: str
    ):
        """Initializes the ModuleModel instance."""
        super().__init__(name, fqmn, file_path, display_namespace, source_namespace)
        
        self.classes: typing.Dict[str, ClassModel] = {}
        self.functions: typing.List[FunctionModel] = []
        self.exported_names: typing.Set[str] = set()

    def add_class(self, class_model: ClassModel) -> None:
        """
        Adds a class to the module.

        Args:
            class_model (ClassModel): The class to be added.
        """
        self.classes[class_model.name] = class_model

    def add_function(self, function_model: FunctionModel) -> None:
        """
        Adds a function to the module.

        Args:
            function_model (FunctionModel): The function to be added.
        """
        self.functions.append(function_model)

# end of file src/org/slashlib/py/apimddoc/core/models/modulemodel.py
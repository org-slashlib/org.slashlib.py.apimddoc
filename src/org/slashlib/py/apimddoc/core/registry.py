# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/core/registry.py
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
import org.slashlib.py.apimddoc.core.models as models
import org.slashlib.py.apimddoc.meta as meta


class ProjectRegistry(metaclass=meta.AutoInitializer):
    """Central registry to store and manage parsed module models."""

    _modules: typing.Dict[str, models.BaseModuleModel] = None
    __is_initialized = False

    @classmethod
    def _class_auto_init_(cls) -> None:
        """Automatically reset the registry state upon class creation."""
        if cls.__is_initialized:
            return
            
        cls._modules = {}
        cls.__is_initialized = True

    @staticmethod
    def is_initialized() -> bool:
        return ProjectRegistry.__is_initialized
        
    @staticmethod
    def register_module(module: models.BaseModuleModel, fqmn: str) -> None:
        """
        Register a parsed module model under its FQMN.

        Args:
            module (models.BaseModuleModel): The module model to store.
            fqmn (str): The fully qualified module name.
        """           
        ProjectRegistry._modules[fqmn] = module

    @staticmethod
    def get_module(fqmn: str) -> typing.Optional[models.BaseModuleModel]:
        """
        Retrieve a registered module by its FQMN.

        Args:
            fqmn (str): The fully qualified module name.

        Returns:
            typing.Optional[models.BaseModuleModel]: The module model if found, else None.
        """           
        return ProjectRegistry._modules.get(fqmn)

    @staticmethod
    def get_root_modules() -> typing.List[models.BaseModuleModel]:
        """
        Retrieve all root modules (modules without a '.' in their FQMN).

        Returns:
            typing.List[models.BaseModuleModel]: List of root modules.
        """           
        return [
            mod for fqmn, mod in ProjectRegistry._modules.items() 
            if "." not in fqmn
        ]

    @staticmethod
    def list_all_modules() -> typing.List[models.BaseModuleModel]:
        """
        Return a list of all registered modules.

        Returns:
            typing.List[models.BaseModuleModel]: List of all modules.
        """            
        return list(ProjectRegistry._modules.values())

# end of file src/org/slashlib/py/apimddoc/core/registry.py
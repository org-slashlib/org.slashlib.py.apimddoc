# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/core/models/basemodel.py
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

class BaseModel:
    """
    Base class for all parsed entities.
    
    This class serves as the foundation for all domain models, providing common 
    metadata like the name, file path, and the Fully Qualified Module Name (FQMN).

    Usage:
        model = BaseModel(name="example", file_path="/path/to/file.py")
        model.fqmn = "org.slashlib.example"  # Output: org.slashlib.example
    """

    def __init__(self, name: str, fqmn: str, file_path: str):
        """
        Initializes the BaseModel instance.

        Args:
            name (str): The name of the entity.
            fqmn (str): The Fully Qualified Module Name.
            file_path (str): The file path where the entity is defined.
        """
        self._fqmn_parts = None
        
        self.name = name
        self.fqmn = fqmn
        self.file_path = file_path

    @property
    def fqmn(self) -> str:
        """Get the Fully Qualified Module Name (e.g., 'org.slashlib.py.core.models')."""
        return ".".join(self._fqmn_parts)

    @fqmn.setter
    def fqmn(self, value: str) -> None:
        """Set the Fully Qualified Module Name by splitting the string into parts."""
        self._fqmn_parts = value.split(".")

    def is_root_model(self) -> bool:
        """Returns True if the entity is a root model (no dots in FQMN)."""
        return len(self._fqmn_parts) == 1

# end of file src/org/slashlib/py/apimddoc/core/models/basemodel.py
# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/core/models/propertymodel.py
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
from org.slashlib.py.apimddoc.core.models.signaturemodel import SignatureModel

class PropertyModel(SignatureModel):
    """
    Represents a parsed property with its metadata.

    Extends SignatureModel to include specific attributes for type hints.

    Args:
        name (str): The name of the entity.
        fqmn (str): The Fully Qualified Module Name.
        file_path (str): The file path where the entity is defined.
        source_namespace (str): The source namespace of the entity.
    """

    def __init__(self, name: str, fqmn: str, file_path: str, source_namespace: str):
        """Initializes the PropertyModel instance."""
        super().__init__(name, fqmn, file_path, source_namespace)
        
        self.type_hint: typing.Optional[str] = None

# end of file src/org/slashlib/py/apimddoc/core/models/propertymodel.py
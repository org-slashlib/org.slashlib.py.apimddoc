# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/core/models/signaturemodel.py
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

class SignatureModel(BaseModel):
    """
    Base class for entities that have a signature/type.

    Extends BaseModel to include specific attributes for entity signatures,
    source namespaces, and associated documentation strings.

    Args:
        name (str): The name of the entity.
        fqmn (str): The Fully Qualified Module Name.
        file_path (str): The file path where the entity is defined.
        source_namespace (str): The source namespace of the entity.
    """

    def __init__(self, name: str, fqmn: str, file_path: str, source_namespace: str):
        """Initializes the SignatureModel instance."""
        super().__init__(name, fqmn, file_path)
        
        self.source_namespace = source_namespace
        self.docstring: typing.Optional[str] = None
        self.signature: typing.Optional[str] = None

# end of file src/org/slashlib/py/apimddoc/core/models/signaturemodel.py
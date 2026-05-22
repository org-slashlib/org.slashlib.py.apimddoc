# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/meta.py
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

"""
Metaclass utilities for automated initialization.

This module provides the AutoInitializer metaclass to automate class-level
setup procedures upon definition.
"""

class AutoInitializer(type):
    """
    A metaclass that automatically triggers initialization methods upon class creation.

    This metaclass inspects the class being created for the presence of specific
    special method (`_class_auto_init_`) and executes it immediately after the
    class object is constructed. 

    Usage:
        class Base(metaclass=AutoInitializer):
            @classmethod
            def _class_auto_init_(cls):
                print(f"Class initialization for {cls.__name__} triggered.")
    """
    def __init__(cls, name, bases, dct):
        """
        Initializes the class and triggers auto-initialization if defined.

        Args:
            cls (type): The class being initialized.
            name (str): The name of the class.
            bases (tuple): A tuple of parent classes.
            dct (dict): The dictionary containing the class namespace.

        Raises:
            TypeError: If _class_auto_init_ is defined in the class but not as a classmethod.
        """
        super().__init__(name, bases, dct)
        # class 'cls' exists at this point.
        
        if '_class_auto_init_' in dct:
            if not isinstance(dct['_class_auto_init_'], classmethod):
                raise TypeError(
                    f"Method '_class_auto_init_' must be a classmethod of class '{name}'."
                )
            cls._class_auto_init_()

# end of file src/org/slashlib/py/apimddoc/meta.py
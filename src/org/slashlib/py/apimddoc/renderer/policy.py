# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/renderer/policy.py
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

import typing
import importlib.metadata
import logging
import pathlib

import org.slashlib.py.apimddoc.meta as meta
from org.slashlib.py.apimddoc.core.models import BaseModel
from org.slashlib.py.apimddoc.core.models import ModuleModel
from org.slashlib.py.apimddoc.core.models import ClassModel
from org.slashlib.py.apimddoc.core.models import FunctionModel
from org.slashlib.py.apimddoc.core.models import NamespaceModuleModel

class RenderingPolicy(metaclass=meta.AutoInitializer):
    """
    Static policy class for deciding on render operations,
    template mapping, and filename generation.
    """

    _log = None
    __is_initialized = False

    @classmethod
    def _class_auto_init_(cls) -> None:
        if cls.__is_initialized:
            return
        cls._log = logging.getLogger(f"org.slashlib.py.apimddoc.{pathlib.Path(__file__).stem}.{cls.__name__}")
        cls.__is_initialized = True
        cls._log.info("Default RenderingPolicy initialized.")

    @classmethod
    def get_policy(cls) -> typing.Type['RenderingPolicy']:
        """
        Locates a custom RenderingPolicy plugin via entry points.
        Falls back to this class if no plugin is registered.
        """
        entry_points = importlib.metadata.entry_points(group='apimddoc.renderer.policy')
        
        if entry_points:
            policy_class = list(entry_points)[0].load()
            cls._log.info("Loaded custom RenderingPolicy plugin.")
            return policy_class
        
        cls._log.info("Using default RenderingPolicy.")
        return cls

    @staticmethod
    def should_render_entity(model: BaseModel) -> bool:
        """
        Determines whether a template should be rendered for the given model.

        Args:
            model (BaseModel): The model entity to check.

        Returns:
            bool: True if the model should be rendered, False otherwise.
        """
        if isinstance(model, NamespaceModuleModel):
            return False
        if isinstance(model, ModuleModel):
            return (len(model.classes) > 0 or 
                    len(model.functions) > 0 or 
                    len(model.exported_names) > 0)
        return isinstance(model, (ClassModel, FunctionModel))

    @staticmethod
    def get_template_name(model: BaseModel) -> str:
        """
        Maps a model instance to the appropriate Jinja2 template filename.

        Args:
            model (BaseModel): The model entity.

        Returns:
            str: The name of the Jinja2 template file.

        Raises:
            ValueError: If no template mapping exists for the given model type.
        """
        if isinstance(model, ModuleModel):
            return "module.md.j2"
        if isinstance(model, ClassModel):
            return "class.md.j2"
        if isinstance(model, FunctionModel):
            return "function.md.j2"
        raise ValueError(f"No template mapped for model type: {type(model)}")

    @staticmethod
    def get_markdown_filename(model: BaseModel) -> str:
        """
        Generates the target filename for a given model based on its FQMN.

        Args:
            model (BaseModel): The model entity.

        Returns:
            str: The generated filename.

        Raises:
            ValueError: If no filename pattern is defined for the given model type.
        """
        if isinstance(model, ModuleModel):
            return f"{model.fqmn}.md"
        if isinstance(model, (ClassModel, FunctionModel)):
            return f"{model.fqmn}.{model.name}.md"
        raise ValueError(f"No filename pattern defined for model type: {type(model)}")

# end of file src/org/slashlib/py/apimddoc/renderer/policy.py
# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/renderer/markdown.py
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

import inspect
import logging
import pathlib
import typing

import jinja2

import org.slashlib.py.apimddoc.meta as meta
import org.slashlib.py.apimddoc.core.registry as registry
from org.slashlib.py.apimddoc.renderer.policy import RenderingPolicy

MODULENAME = pathlib.Path(__file__).stem

# setup logging
log = logging.getLogger(f"org.slashlib.py.apimddoc.{MODULENAME}")


class MarkdownRenderer(metaclass=meta.AutoInitializer):
    """Renderer that transforms registry models into Markdown using Jinja2 templates."""

    _env: typing.Optional[jinja2.Environment] = None
    _log = None
    __is_initialized = False

    @classmethod
    def _class_auto_init_(cls) -> None:
        if cls.__is_initialized:
            return
            
        cls._log = logging.getLogger(f"org.slashlib.py.apimddoc.{MODULENAME}.{cls.__name__}")
        cls.__is_initialized = True
        cls._log.info("MarkdownRenderer initialized.")

    @staticmethod
    def is_initialized() -> bool:
        return MarkdownRenderer.__is_initialized

    @classmethod
    def setup(cls, template_dir: str) -> None:
        """
        Configures the renderer environment and logs the template directory.

        Args:
            template_dir (str): Path to the folder containing .j2 templates.
        """
        cls._log.debug(f"{cls.__name__}.{inspect.currentframe().f_code.co_name}: Setting up MarkdownRenderer with template directory: {template_dir}")
        cls._env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            autoescape=False
        )

    @classmethod
    def _get_template(cls, template_name: str) -> jinja2.Template:
        """
        Loads a template from the environment and logs the access.

        Args:
            template_name (str): The filename of the template (e.g., 'module.md.j2').

        Returns:
            jinja2.Template: The loaded Jinja2 template.
        """
        cls._log.info(f"{cls.__name__}.{inspect.currentframe().f_code.co_name}: Loading template: {template_name}")
        return cls._env.get_template(template_name)

    @staticmethod
    def render(output_dir: str) -> None:
        """
        Generates the Markdown documentation for all registered modules using the active RenderingPolicy.

        Args:
            output_dir (str): The directory where the Markdown files should be saved.
        """
        MarkdownRenderer._log.debug(f"{MarkdownRenderer.__name__}.{inspect.currentframe().f_code.co_name}: rendering to `{output_dir}`")
        
        if not MarkdownRenderer._env:
            raise RuntimeError("MarkdownRenderer not configured. Call setup() first.")
            
        policy_cls = RenderingPolicy.get_policy()
        output_path = pathlib.Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        for model in registry.ProjectRegistry.list_all_modules():
            if policy_cls.should_render_entity(model):
                MarkdownRenderer._log.info(f"{MarkdownRenderer.__name__}.{inspect.currentframe().f_code.co_name}: rendering model {model}")
                template = MarkdownRenderer._get_template(policy_cls.get_template_name(model))
                
                # Retrieve and normalize the target filename
                filename = policy_cls.get_markdown_filename(model)
                normalized_filename = pathlib.Path(filename)
                
                content = template.render(model=model)
                
                # Ensure the directory structure exists for the target file
                target_file = output_path / normalized_filename
                target_file.parent.mkdir(parents=True, exist_ok=True)
                
                target_file.write_text(content, encoding="utf-8")
                MarkdownRenderer._log.info(f"Rendered: {filename}")
            else:
                MarkdownRenderer._log.info(f"{MarkdownRenderer.__name__}.{inspect.currentframe().f_code.co_name}: not rendering model {model}")

# end of file src/org/slashlib/py/apimddoc/renderer/markdown.py
# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/parser/parser.py
# @AI:
# - INTEGRITY RULES:
#   - STRICT PRESERVATION: Do not remove, move, or modify ANY existing lines of code or comments 
#     unless they are the explicit target of the requested change. 
#   - DEBUG MARKERS: Commented-out code (e.g., debug prints) MUST be kept exactly where they are.
#   - WHITESPACE & STRUCTURE: Maintain all original empty lines and the existing file structure. 
#     Structural integrity takes precedence over "clean code" or "elegance".
#   - LEAD-IN/OUT: The very first and last lines (all comments in between) are immutable anchors.
# - MAINTENANCE:
#   - Only update pydoc strings (args, returns, raises) if the function signature changes.
#   - Do NOT delete existing examples or descriptions in pydoc.
# - LANGUAGE: en-US for all comments and documentation.
#

import pathlib
import typing
import ast

from org.slashlib.py.apimddoc.core.registry import ProjectRegistry
from org.slashlib.py.apimddoc.crawler import SourceCrawler
from org.slashlib.py.apimddoc.parser.filevisitor import FileVisitor
from org.slashlib.py.apimddoc.core.models.modulemodel import ModuleModel
from org.slashlib.py.apimddoc.core.models.namespacemodulemodel import NamespaceModuleModel


class ASTParser:
    """
    Parser that orchestrates the registry tree construction and subsequent 
    AST-based analysis of Python files.
    """

    def __init__(self, root_path: pathlib.Path):
        """
        Initializes the ASTParser with the project root path.

        Args:
            root_path (pathlib.Path): The absolute path to the project root.
        """
        self.root_path = root_path

    def parse(self, file_paths: typing.List[pathlib.Path]) -> None:
        """
        Coordinates the parsing process by building the registry structure
        and then parsing individual files.

        Args:
            file_paths (typing.List[pathlib.Path]): List of .py files to process.
        """
        for file_path in file_paths:
            self.parsePath(file_path)
            self.parseFile(file_path)

    def parsePath(self, file_path: pathlib.Path) -> None:
        """
        Decomposes a file path and initiates the recursive registry construction.
        The file itself is excluded from the segments, as it is handled by parseFile.

        Args:
            file_path (pathlib.Path): The path to the file currently being processed.
        """
        relative_path = file_path.relative_to(self.root_path)
        # Exclude the file name itself (last element) as it is handled by parseFile
        segments = list(relative_path.parent.parts)
        
        parent_module = None
        current_fqmn_parts = []

        for i, segment in enumerate(segments):
            parent_module = self.parsePathSegment(
                segment, i, segments, file_path, current_fqmn_parts, parent_module
            )

    def parsePathSegment(
        self, 
        segment: str, 
        index: int, 
        segments: typing.List[str], 
        file_path: pathlib.Path, 
        current_fqmn_parts: typing.List[str], 
        parent_module: typing.Optional[typing.Any]
    ) -> typing.Any:
        """
        Processes a single path segment and ensures the corresponding module model
        exists in the registry.

        Args:
            segment (str): The current path segment name.
            index (int): The index of the current segment.
            segments (typing.List[str]): All path segments (excluding the file itself).
            file_path (pathlib.Path): The original file path.
            current_fqmn_parts (typing.List[str]): List collecting FQMN parts.
            parent_module (Optional[Any]): The parent module model.

        Returns:
            Any: The module model corresponding to this segment.
        """
        current_fqmn_parts.append(segment)
        fqmn = ".".join(current_fqmn_parts)
        
        module = ProjectRegistry.get_module(fqmn)
        
        if not module:
            current_phys_path = self.root_path.joinpath(*segments[:index+1])
            
            if SourceCrawler.is_package(current_phys_path):
                module = ModuleModel(
                    name=segment, fqmn=fqmn, file_path=str(current_phys_path),
                    display_namespace=fqmn, source_namespace=fqmn
                )
            else:
                module = NamespaceModuleModel(
                    name=segment, fqmn=fqmn, file_path=str(current_phys_path),
                    display_namespace=fqmn, source_namespace=fqmn
                )
            
            ProjectRegistry.register_module(module, fqmn)
            if parent_module:
                parent_module.add_submodule(module)
        
        return module

    def parseFile(self, file_path: pathlib.Path) -> None:
        """
        Parses the AST of a single file and populates the module model.

        Args:
            file_path (pathlib.Path): The path to the file to be parsed.
        """
        fqmn = SourceCrawler.get_module_namespace(file_path)
        module_model = ProjectRegistry.get_module(fqmn)
        
        if module_model:
            with open(file_path, "r", encoding="utf-8") as source:
                tree = ast.parse(source.read())
                visitor = FileVisitor(module_model)
                visitor.visit(tree)


# end of file src/org/slashlib/py/apimddoc/parser/parser.py
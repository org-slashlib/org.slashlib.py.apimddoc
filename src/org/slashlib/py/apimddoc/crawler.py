# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/crawler.py
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
import pathlib
import logging
import typing

# internal imports
import org.slashlib.py.apimddoc.bootstrap as bootstrap
import org.slashlib.py.apimddoc.meta as meta


class SourceCrawler(metaclass=meta.AutoInitializer):
    """
    Crawls the project source directories to identify all Python modules 
    and packages, including namespace packages.

    Design Decision:
    This class is implemented using static methods rather than instance methods.
    Since the Crawler operates on global project configurations (source roots)
    defined in 'pyproject.toml', a single, stateless service pattern is 
    optimal. This avoids unnecessary object instantiation and ensures that 
    the project configuration is initialized and managed consistently across 
    the entire application lifecycle.
    """

    _log = None
    _source_roots: typing.Optional[typing.Tuple[pathlib.Path, ...]] = None
    __is_initialized = False

    @classmethod
    def _class_auto_init_(cls) -> None:
        """
        Initialize the crawler by loading source roots from bootstrap.

        Returns:
            None
        """
        if cls.__is_initialized:
            if cls._log:
                cls._log.debug("Crawler already initialized. Skipping redundant initialization.")
            return
        
        cls._log = logging.getLogger(f"org.slashlib.py.apimddoc.{pathlib.Path(__file__).stem}.{cls.__name__}")
        
        # Convert source roots to pathlib.Path objects
        raw_roots = bootstrap.get_source_roots()
        cls._source_roots = tuple(pathlib.Path(root) for root in raw_roots)

        cls._log.info(f"Initialized crawler with roots: {cls._source_roots}")
        cls.__is_initialized = True

    @staticmethod
    def is_initialized() -> bool:
        """
        Returns true, if `auto init` was run.

        Returns:
            bool: True if initialized, False otherwise.
        """
        return SourceCrawler.__is_initialized

    @staticmethod
    def is_package(path: pathlib.Path) -> bool:
        """
        Checks if a directory is a Python package (contains __init__.py).

        Args:
            path (pathlib.Path): The directory path to check.

        Returns:
            bool: True if the path is a directory and contains __init__.py.
        """
        if path.is_dir():
            return (path / "__init__.py").exists()
        return False

    @staticmethod
    def get_all_python_files() -> typing.List[pathlib.Path]:
        """
        Performs a recursive search for all .py files in all initialized source roots.

        Returns:
            typing.List[pathlib.Path]: A list of all discovered Python files.
        """
        python_files = []
        for root in SourceCrawler._source_roots:
            SourceCrawler._log.info(f"Crawling source root: {root}")
            python_files.extend(list(root.rglob("*.py")))
        
        SourceCrawler._log.info(f"Found {len(python_files)} python files in total.")
        return python_files

    @staticmethod
    def get_module_namespace(file_path: pathlib.Path) -> str:
        """
        Converts a file path to a fully qualified module name based 
        on the corresponding source root.

        Args:
            file_path (pathlib.Path): The path to the file.

        Returns:
            str: The fully qualified module name (e.g., org.slashlib.py.module).

        Raises:
            ValueError: If the file path does not reside within any of the configured source roots.
        """
        # Find which source root this file belongs to
        for root in SourceCrawler._source_roots:
            if root in file_path.parents or root == file_path.parent:
                relative_path = file_path.relative_to(root)
                
                # Remove suffix and convert path separators to dots
                parts = list(relative_path.with_suffix("").parts)
                
                # Handle __init__ files: if the last part is __init__, pop it
                if parts[-1] == "__init__":
                    parts.pop()
                    
                return ".".join(parts)
        
        raise ValueError(f"File {file_path} does not belong to any known source root.")

# end of file src/org/slashlib/py/apimddoc/crawler.py
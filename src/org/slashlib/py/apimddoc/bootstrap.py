# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/bootstrap.py
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
import logging
import pathlib
import sys
import typing

if sys.version_info >= (3, 11):
    import tomllib # pragma: no cover - python version is not subject to testing
else:
    import tomli as tomllib # pragma: no cover - python version is not subject to testing

# setup logging
log = logging.getLogger(f"org.slashlib.py.apimddoc.{pathlib.Path(__file__).stem}")

def get_pyproject_path() -> pathlib.Path:
    """
    Locates the pyproject.toml file in the current working directory.

    Returns:
        pathlib.Path: The absolute path to the found pyproject.toml.

    Raises:
        FileNotFoundError: If no pyproject.toml is found in the current working directory.
    """
    pyproject = pathlib.Path.cwd() / "pyproject.toml"
    if not pyproject.exists():
        raise FileNotFoundError("Could not find pyproject.toml in the current working directory.")
    return pyproject

def get_project_config() -> dict:
    """
    Reads the pyproject.toml and returns its content as a dictionary.

    Returns:
        dict: The configuration content of pyproject.toml.
    """
    pyproject = get_pyproject_path()
    with open(pyproject, "rb") as f:
        return tomllib.load(f)

def get_source_roots() -> typing.Tuple[str, ...]:
    """
    Locates the project root and returns all source directories
    defined in pyproject.toml as POSIX strings.

    Returns:
        typing.Tuple[str, ...]: A tuple of relative POSIX path strings.

    Raises:
        ValueError: If the configuration structure is missing.
    """
    config = get_project_config()

    # Extract [tool.setuptools.packages.find] configuration
    try:
        # Navigate the config dictionary safely
        where_dirs = config["tool"]["setuptools"]["packages"]["find"]["where"]
    except KeyError:
        raise ValueError("pyproject.toml: Missing `[tool.setuptools.packages.find] where` configuration.")

    if isinstance(where_dirs, str):
        return (pathlib.Path(where_dirs).as_posix(),)
    
    return tuple(pathlib.Path(d).as_posix() for d in where_dirs)

def get_resolved_source_roots() -> typing.Tuple[str, ...]:
    """
    Returns the source directories defined in pyproject.toml as absolute paths 
    represented as POSIX strings.

    Returns:
        typing.Tuple[str, ...]: A tuple of absolute paths as POSIX strings.
    """
    # Base directory is the directory containing the pyproject.toml
    base_dir = get_pyproject_path().parent
    roots = get_source_roots()
    
    # Resolve the paths and return as POSIX strings
    return tuple((base_dir / root).resolve().as_posix() for root in roots)

# end of file src/org/slashlib/py/apimddoc/bootstrap.py
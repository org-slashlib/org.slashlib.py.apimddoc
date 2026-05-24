# -*- coding: utf-8 -*-
# file src/org/slashlib/py/apimddoc/cli.py
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

# python imports
import argparse
import logging
import pathlib
import importlib.resources
import typing

# third party imports
import org.slashlib.py.configloader

# internal imports
import org.slashlib.py.apimddoc.core.registry as registry
from org.slashlib.py.apimddoc.renderer.markdown import MarkdownRenderer as renderer
import org.slashlib.py.apimddoc.bootstrap as bootstrap
from org.slashlib.py.apimddoc.crawler import SourceCrawler as crawler
import org.slashlib.py.apimddoc.parser.parser as parser

# setup logging
log = logging.getLogger(f"org.slashlib.py.apimddoc.{pathlib.Path(__file__).stem}")

def _find_template_dir(resolved_roots: typing.Tuple[str, ...]) -> typing.Optional[pathlib.Path]:
    """
    Iterates through resolved source roots to find the 'templates' directory.

    Args:
        resolved_roots (typing.Tuple[str, ...]): Tuple of absolute POSIX paths.

    Returns:
        typing.Optional[pathlib.Path]: The path to the templates directory if found, 
                                       otherwise None.
    """
    for root_str in resolved_roots:
        # Resolve absolute path from POSIX string and locate potential template dir
        source_root = pathlib.Path(root_str)
        potential_path = source_root.parent.parent / "templates"
        
        log.debug(f"Checking for templates at: {potential_path}")
        
        if potential_path.exists():
            return potential_path
            
    return None

def _get_template_dir(resolved_roots: typing.Tuple[str, ...]) -> pathlib.Path:
    """
    Determines the template directory path by checking resolved source roots.

    Returns:
        pathlib.Path: The resolved path to the Jinja2 templates.
    """
    try:
        found_path = _find_template_dir(resolved_roots)
        
        if found_path:
            return found_path
            
        log.warning("Could not find local templates in source roots. Falling back to template resources of `org.slashlib.py.apimddoc`.")
    except Exception as e:
        log.warning(f"Error while determining template directory: {e}. Falling back to template resources of `org.slashlib.py.apimddoc`.")
            
    # Fallback to package resources
    return importlib.resources.files("org.slashlib.py.apimddoc").joinpath("templates")

def main(output_dir: str = None) -> None:
    """
    Main entry point for the CLI tool.
    
    Coordinates the registry initialization, parsing and rendering process.
    """
    # 1. Get Template Directory
    resolved_roots = bootstrap.get_resolved_source_roots()
    template_dir = _get_template_dir(resolved_roots)

    # 2. Use SourceCrawler to gather all files
    # FUTURE: (maybe) - source directories
    # Determine input path: use provided arg or default to current directory
    # input_path = pathlib.Path(args.input) if args.input else bootstrap.get_pyproject_path().parent
    # all_files = crawler.get_all_python_files(input_path)
    all_files = crawler.get_all_python_files()

    # 3. Parse source files
    log.info("Starting parsing process.")
    ast_parser = parser.ASTParser(root_path=bootstrap.get_pyproject_path().parent)
    ast_parser.parse(all_files)
    log.info("Parsing process completed.")

    # 4. Dependency Injection
    log.info(f"Initializing registry and renderer. Using template dir: {template_dir}")
    renderer.setup(str(template_dir))

    # 5. Evaluate output directory
    if output_dir is None:
        output_dir = bootstrap.get_pyproject_path().parent / "docs"
    
    output_path = pathlib.Path(output_dir)
    log.info(f"Rendering documentation to: {output_path}")   
    output_path.mkdir(parents=True, exist_ok=True)

    # 6. Render to output directory   
    renderer.render(str(output_path))
    log.info("Documentation rendered successfully.")

if __name__ == "__main__": # pragma: no cover
    arg_parser = argparse.ArgumentParser(description="API Documentation Generator")
    # FUTURE: (maybe) - currently we crawl the source directories specified by pyproject.toml
    # arg_parser.add_argument("-input", help="Input directory of source code")
    arg_parser.add_argument("-output", help="Output directory for documentation")
    args = arg_parser.parse_args()

    main(output_dir=args.output)
    
# end of file src/org/slashlib/py/apimddoc/cli.py
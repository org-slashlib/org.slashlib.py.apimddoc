# -*- coding: utf-8 -*-
# file test/03_01_03_cli_main_test.py
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
Module: cli.py
Class: N/A (Standalone function)
Function: main
Special Considerations: 
- Mocks bootstrap and registry to isolate the CLI orchestration logic.
- Verifies that the main entry point executes without exception.
"""

import pytest
from org.slashlib.py.apimddoc.cli import main

def test_import_integrity():
    """
    What: Verify the integrity of the test object.
    Why: Ensure the function is importable and callable.
    """
    assert callable(main), "main must be a function"

def test_main_execution(monkeypatch):
    """
    What: Verify that main() executes the coordination flow.
    Why: To ensure that the orchestration (bootstrap, template, registry) is invoked correctly.
    """
    # 1. Mock bootstrap calls
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_resolved_source_roots", lambda: ("/tmp/src",))
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_source_roots", lambda: ("src",))
    
    # 2. Mock template directory lookup to avoid real filesystem dependency
    monkeypatch.setattr("org.slashlib.py.apimddoc.cli._get_template_dir", lambda x: "/tmp/templates")
    
    # 3. Mock registry and renderer to avoid complex object initialization
    monkeypatch.setattr("org.slashlib.py.apimddoc.core.registry.ProjectRegistry", lambda: None)
    monkeypatch.setattr("org.slashlib.py.apimddoc.renderer.markdown.MarkdownRenderer", lambda reg, path: None)
    
    # 4. Execute main
    # main() parses sys.argv, so we don't need extra setup for basic execution
    main()

# end of file test/03_01_03_cli_main_test.py
# -*- coding: utf-8 -*-
# file test/04_00_01___main____main_test.py
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
Module: __main__.py
Class: N/A
Function: N/A (Script execution)
Special Considerations: 
- Tests the entry point of the application execution flow using runpy.
- Verifies that the CLI orchestration is correctly triggered.
"""

import pytest
import runpy
from unittest.mock import patch

def test_main_call():
    """
    What: Verify that running __main__ as a script triggers cli.main().
    Why: To ensure that the package entry point correctly invokes the CLI orchestration.
    """
    # We mock the main function in the module that __main__ now imports and calls
    with patch("org.slashlib.py.apimddoc.cli.main") as mocked_main:
        # runpy simulates the execution as if it were called via 'python -m ...'
        try:
            runpy.run_module("org.slashlib.py.apimddoc.__main__", run_name="__main__")
        except SystemExit:
            # Catch SystemExit if main() or argparse triggers it
            pass
        
        # Verify that cli.main() was called exactly once
        mocked_main.assert_called_once()

# end of file test/04_00_01___main____main_test.py
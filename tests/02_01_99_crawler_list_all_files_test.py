# -*- coding: utf-8 -*-
# file test/02_01_99_crawler_list_all_files_test.py
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
Module: crawler.py
Class: SourceCrawler
Method: get_all_python_files
Special Considerations:
- Directly calls get_all_python_files to list files in the configured project structure.
- Reality check 😎
"""

from org.slashlib.py.apimddoc.crawler import SourceCrawler

def test_list_all_python_files():
    """
    What: List all .py files discovered by the SourceCrawler.
    Why: Verify that the crawler finds files based on initialized source roots.
    
    Run: pytest -s .\tests\02_01_99_crawler_list_all_files_test.py to see results.
    """
    # Ensure crawler is initialized (handled by metaclass/bootstrap)
    files = SourceCrawler.get_all_python_files()
    
    # Print results to console as requested
    for file_path in files:
        print(file_path)

# end of file test/02_01_99_crawler_list_all_files_test.py
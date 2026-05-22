# -*- coding: utf-8 -*-
# file test/02_01_03_crawler_sourcecrawler_get_all_python_files_test.py
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
- This test suite ensures the Crawler correctly identifies Python files across multiple source roots.
- Design Decisions:
    1. Recursive Search: The test ensures files in subdirectories are also discovered.
    2. Dependency Injection: We manually inject _source_roots and _log to avoid
       dependency on the actual bootstrap/init logic during pure method testing.
"""

import pytest
import pathlib
import logging
from org.slashlib.py.apimddoc.crawler import SourceCrawler

def test_get_all_python_files(tmp_path):
    """
    What: Verify that all .py files in source roots are found.
    Why: Ensure the recursive file discovery works correctly.
    """
    # 1. Setup mock structure: src1/a.py, src1/sub/b.py, src2/c.py
    src1 = tmp_path / "src1"
    src2 = tmp_path / "src2"
    src1.mkdir()
    (src1 / "sub").mkdir()
    src2.mkdir()
    
    (src1 / "a.py").touch()
    (src1 / "sub" / "b.py").touch()
    (src2 / "c.py").touch()
    (src1 / "notes.txt").touch() # Should be ignored
    
    # 2. Inject state directly to bypass bootstrap/initializer dependencies
    SourceCrawler._source_roots = (src1, src2)
    SourceCrawler._log = logging.getLogger("test_logger")
    
    # 3. Get files
    files = SourceCrawler.get_all_python_files()
    
    # 4. Assert
    assert len(files) == 3
    assert any(f.name == "a.py" for f in files)
    assert any(f.name == "b.py" for f in files)
    assert any(f.name == "c.py" for f in files)

# end of file test/02_01_03_crawler_sourcecrawler_get_all_python_files_test.py
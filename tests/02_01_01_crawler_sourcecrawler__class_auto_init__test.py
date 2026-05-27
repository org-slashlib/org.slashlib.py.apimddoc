# -*- coding: utf-8 -*-
# file test/02_01_01_crawler_sourcecrawler__class_auto_init__test.py
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
Method: _class_auto_init_

Special Considerations:
- This test suite verifies the internal lazy initialization of the SourceCrawler.
- Design Decisions:
    1. Indirect Validation: Verify side effects (attributes) and the public status method.
    2. State Management: The test environment resets internal state using name mangling 
       to force a fresh initialization.
    3. AutoInitializer Integration: The first initialization occurs automatically 
       via meta.AutoInitializer upon importing SourceCrawler.
"""

import pytest
import logging
import pathlib
from org.slashlib.py.apimddoc.crawler import SourceCrawler

def test_sourcecrawler_class_auto_init_integrity():
    """
    What: Verify the integrity of the test object (importability and type check).
    Why: Mandatory first test for every Testsuite.
    """
    assert SourceCrawler is not None
    assert isinstance(SourceCrawler, type)

def test_sourcecrawler_class_auto_init_success(monkeypatch, tmp_path):
    """
    What: Verify that _class_auto_init_ populates class state correctly.
    Why: Ensure the crawler internal state is correctly initialized on first run.
    """
    # 1. Setup mock
    mock_roots = (tmp_path,)
    monkeypatch.setattr("org.slashlib.py.apimddoc.bootstrap.get_source_roots", lambda: mock_roots)

    # 2. Reset state (Using name mangling to reach the real internal flag)
    SourceCrawler._log = None
    SourceCrawler._source_roots = None
    setattr(SourceCrawler, "_SourceCrawler__is_initialized", False)
    
    # 3. Trigger initialization
    SourceCrawler._class_auto_init_()
    
    # 4. Assert state via public/safe attributes and methods
    assert SourceCrawler.is_initialized() is True
    assert SourceCrawler._log is not None
    assert SourceCrawler._source_roots == mock_roots

def test_sourcecrawler_class_auto_init_redundant_call():
    """
    What: Verify that calling _class_auto_init_ a second time logs a debug message 
          and returns immediately (redundant initialization).
    Why: Ensure the initialization logic is idempotent and robust.
    """
    # 1. Reset state
    setattr(SourceCrawler, "_SourceCrawler__is_initialized", False)
    
    # 2. Setup local logger to capture messages
    logger_name = "org.slashlib.py.apimddoc.crawler.SourceCrawler"
    logger = logging.getLogger(logger_name)
    logger.handlers = []
    
    captured_messages = []
    class TestHandler(logging.Handler):
        def emit(self, record):
            captured_messages.append(record.getMessage())
            
    logger.addHandler(TestHandler())
    logger.setLevel(logging.DEBUG)
    SourceCrawler._log = logger
    
    # 3. Trigger initial and redundant initialization
    SourceCrawler._class_auto_init_()
    SourceCrawler._class_auto_init_()
    
    # 4. Assert that the debug message was logged
    assert any("Crawler already initialized" in msg for msg in captured_messages)

# end of file test/02_01_01_crawler_sourcecrawler__class_auto_init__test.py
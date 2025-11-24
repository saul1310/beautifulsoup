
# Milestone 4: Iterable BeautifulSoup
     
     ## What's New
     - Added the iterator protocol (`__iter__` and `__next__`) to the BeautifulSoup class
     - BeautifulSoup objects can now be iterated with `for` loops
     - Tree traversal without collecting all nodes into a list, as specified in canvas
     
     ## Features
     - Depth-first traversal of parse tree
     - Memory-efficient iteration using generators
     - Works with all HTML/XML documents
     
     ## Tests
     - 5 comprehensive test cases covering:
       - Simple iteration
       - Nested structures
       - Empty documents
       - Node counting
       - Filtering during iteration
     
     ## Files Modified
     - `bs4/__init__.py` - Added `__iter__()` and `__next__()` methods
     
     ## New Files
     - `Milestone4/test_simple_iteration.py`
     - `Milestone4/test_nested_iteration.py`
     - `Milestone4/test_empty_iteration.py`
     - `Milestone4/test_node_counting.py`
     - `Milestone4/test_filter_during_iteration.py`
     - `Milestone4/M4-README.md`
```





After publishing, you'll see your release. The URL will be:
```
https://github.com/YOUR-USERNAME/beautifulsoup/releases/tag/milestone-4

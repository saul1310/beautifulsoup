#!/usr/bin/env python3
"""
Test 4: Count specific types of nodes during iteration
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup
from bs4.element import Tag

def test_node_counting():
    """Test counting nodes of specific types during iteration."""
    print("="*70)
    print("TEST 4: Node Type Counting")
    print("="*70)
    
    html = """
    <html>
        <body>
            <p>First</p>
            <div>Middle</div>
            <p>Last</p>
            <span>Span</span>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Count specific tag types
    tag_counts = {}
    for node in soup:
        if isinstance(node, Tag):
            name = node.name
            tag_counts[name] = tag_counts.get(name, 0) + 1
    
    print("Tag counts:")
    for tag_name, count in sorted(tag_counts.items()):
        print(f"  <{tag_name}>: {count}")
    
    # Verify expected tags
    expected = {'html': 1, 'body': 1, 'p': 2, 'div': 1, 'span': 1}
    
    passed = True
    for tag, expected_count in expected.items():
        actual_count = tag_counts.get(tag, 0)
        if actual_count == expected_count:
            print(f"✓ Found {expected_count} <{tag}> tag(s)")
        else:
            print(f"✗ Expected {expected_count} <{tag}>, found {actual_count}")
            passed = False
    
    if passed:
        print("\n✓ TEST 4 PASSED\n")
    else:
        print("\n✗ TEST 4 FAILED\n")
    
    return passed

if __name__ == "__main__":
    success = test_node_counting()
    sys.exit(0 if success else 1)
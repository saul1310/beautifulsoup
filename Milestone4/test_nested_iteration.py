#!/usr/bin/env python3
"""
Test 3: Nested structure iteration
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

def test_nested_iteration():
    """Test iteration over deeply nested structures."""
    print("="*70)
    print("TEST 3: Nested Structure Iteration")
    print("="*70)
    
    html = """
    <div class="container">
        <div class="level1">
            <div class="level2">
                <p>Deep content</p>
            </div>
            <p>Level1 content</p>
        </div>
    </div>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Collect all nodes
    all_nodes = list(soup)
    print(f"Total nodes: {len(all_nodes)}")
    
    # Count tags and text nodes
    tags = [n for n in all_nodes if isinstance(n, Tag)]
    text_nodes = [n for n in all_nodes if isinstance(n, NavigableString) and not isinstance(n, Tag)]
    
    print(f"  Tags: {len(tags)}")
    print(f"  Text nodes: {len(text_nodes)}")
    
    # Verify structure
    if len(all_nodes) > 0:
        print("✓ Deep nesting produces nodes")
    else:
        print("✗ No nodes produced from deeply nested structure")
        return False
    
    # Check for expected tags
    tag_names = [t.name for t in tags]
    
    expected_tags = ['div', 'div', 'div', 'p', 'p']
    if all(tag in tag_names for tag in ['div', 'p']):
        print("✓ Found expected tag types (div, p)")
    else:
        print(f"✗ Missing expected tags. Found: {set(tag_names)}")
        return False
    
    # Verify we can iterate multiple times
    count1 = len(list(soup))
    count2 = len(list(soup))
    
    if count1 == count2:
        print(f"✓ Consistent nested iteration: {count1} nodes each pass")
    else:
        print(f"✗ Inconsistent nested iteration: {count1} vs {count2}")
        return False
    
    print("\n✓ TEST 3 PASSED\n")
    return True

if __name__ == "__main__":
    success = test_nested_iteration()
    sys.exit(0 if success else 1)

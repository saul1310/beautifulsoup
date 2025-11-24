#!/usr/bin/env python3
"""
Test 5: Filtering nodes during iteration
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

def test_filter_during_iteration():
    """Test filtering and processing nodes while iterating."""
    print("="*70)
    print("TEST 5: Filtering During Iteration")
    print("="*70)
    
    html = """
    <html>
        <body>
            <p class="highlight">Important</p>
            <p>Normal</p>
            <p class="highlight">Also important</p>
            <div>Container</div>
            <span class="highlight">Span text</span>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Filter for tags with "highlight" class
    highlighted = []
    for node in soup:
        if isinstance(node, Tag) and 'highlight' in node.get('class', []):
            highlighted.append(node)
    
    print(f"Total highlighted nodes: {len(highlighted)}")
    
    if len(highlighted) == 3:
        print("✓ Found all 3 highlighted nodes")
    else:
        print(f"✗ Expected 3 highlighted nodes, found {len(highlighted)}")
        return False
    
    # Filter for text nodes only
    text_nodes = []
    for node in soup:
        if isinstance(node, NavigableString) and not isinstance(node, Tag):
            text = node.strip()
            if text:  # Only non-empty text
                text_nodes.append(text)
    
    print(f"Total non-empty text nodes: {len(text_nodes)}")
    
    if len(text_nodes) > 0:
        print("✓ Found text nodes")
        print(f"  Samples: {text_nodes[:3]}")
    else:
        print("✗ No text nodes found")
        return False
    
    # Filter for specific tag types
    p_tags = []
    for node in soup:
        if isinstance(node, Tag) and node.name == 'p':
            p_tags.append(node)
    
    print(f"Total <p> tags: {len(p_tags)}")
    
    if len(p_tags) == 3:
        print("✓ Found all 3 <p> tags")
    else:
        print(f"✗ Expected 3 <p> tags, found {len(p_tags)}")
        return False
    
    print("\n✓ TEST 5 PASSED\n")
    return True

if __name__ == "__main__":
    success = test_filter_during_iteration()
    sys.exit(0 if success else 1)

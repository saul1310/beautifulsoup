#!/usr/bin/env python3
"""
Test 1: Simple iteration over basic HTML structure
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup

def test_simple_iteration():
    """Test iteration over a simple HTML document."""
    print("="*70)
    print("TEST 1: Simple Iteration")
    print("="*70)
    
    html = """
    <html>
        <head><title>Test</title></head>
        <body>
            <p>Paragraph 1</p>
            <p>Paragraph 2</p>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Collect nodes by iterating
    nodes = []
    for node in soup:
        nodes.append(node)
    
    print(f"Total nodes found: {len(nodes)}")
    
    # Verify we got nodes
    if len(nodes) > 0:
        print("✓ Iteration produced nodes")
    else:
        print("✗ No nodes produced")
        return False
    
    # Verify we can iterate multiple times
    count1 = sum(1 for _ in soup)
    count2 = sum(1 for _ in soup)
    
    if count1 == count2:
        print(f"✓ Consistent iteration count: {count1}")
    else:
        print(f"✗ Inconsistent counts: {count1} vs {count2}")
        return False
    
    print("\n✓ TEST 1 PASSED\n")
    return True

if __name__ == "__main__":
    success = test_simple_iteration()
    sys.exit(0 if success else 1)
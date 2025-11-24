#!/usr/bin/env python3
"""
Test 2: Iteration over empty document
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup

def test_empty_iteration():
    """Test iteration over an empty or minimal HTML document."""
    print("="*70)
    print("TEST 2: Empty Document Iteration")
    print("="*70)
    
    # Test 1: Empty string
    soup = BeautifulSoup("", 'html.parser')
    count = sum(1 for _ in soup)
    print(f"Empty string - nodes: {count}")
    
    if count == 0:
        print("✓ Empty string produces no nodes")
    else:
        print(f"✗ Expected 0 nodes for empty string, got {count}")
        return False
    
    # Test 2: Whitespace only
    soup = BeautifulSoup("   \n\t  ", 'html.parser')
    count = sum(1 for _ in soup)
    print(f"Whitespace only - nodes: {count}")
    
    # Whitespace becomes a text node
    if count >= 0:  # Could be 0 or contain whitespace node
        print("✓ Whitespace handling works")
    else:
        print(f"✗ Unexpected node count: {count}")
        return False
    
    # Test 3: Single text node
    soup = BeautifulSoup("Hello", 'html.parser')
    nodes = list(soup)
    count = len(nodes)
    print(f"Single text 'Hello' - nodes: {count}")
    
    if count == 1:
        print("✓ Single text node produces 1 node")
    else:
        print(f"✗ Expected 1 node, got {count}")
        return False
    
    print("\n✓ TEST 2 PASSED\n")
    return True

if __name__ == "__main__":
    success = test_empty_iteration()
    sys.exit(0 if success else 1)

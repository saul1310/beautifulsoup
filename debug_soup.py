#!/usr/bin/env python3
"""Debug script to understand BeautifulSoup structure"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
beautifulsoup_path = os.path.join(current_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup

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

print("=" * 70)
print("DEBUG: BeautifulSoup Object Structure")
print("=" * 70)

# Check class hierarchy
print(f"\nBeautifulSoup inherits from: {BeautifulSoup.__bases__}")

# Check if it has _root attribute
print(f"\nHas '_root' attribute: {hasattr(soup, '_root')}")
if hasattr(soup, '_root'):
    print(f"  _root value: {soup._root}")

# Check if it has descendants (inherited from Tag)
print(f"\nHas 'descendants' attribute: {hasattr(soup, 'descendants')}")
if hasattr(soup, 'descendants'):
    print(f"  descendants type: {type(soup.descendants)}")
    try:
        descendants_list = list(soup.descendants)
        print(f"  Number of descendants: {len(descendants_list)}")
        print(f"  First 5 descendants:")
        for i, desc in enumerate(descendants_list[:5]):
            print(f"    {i}: {repr(desc)[:50]}")
    except Exception as e:
        print(f"  Error calling descendants: {e}")

# Check relevant attributes
relevant_attrs = ['contents', 'children', 'name', 'tag_stack', 'tagStack']
print("\nRelevant attributes:")
for attr in relevant_attrs:
    if hasattr(soup, attr):
        val = getattr(soup, attr)
        print(f"  {attr}: {type(val)} = {repr(val)[:60]}")

# Check if soup.name is the root tag
print(f"\nsoup.name: {soup.name}")

# Try direct iteration
print("\n" + "=" * 70)
print("Testing iteration:")
print("=" * 70)

count = 0
for node in soup:
    count += 1
    if count <= 5:
        print(f"  Node {count}: {repr(node)[:50]}")

print(f"\nTotal nodes from iteration: {count}")

# Check children
print("\n" + "=" * 70)
print("Testing soup.children:")
print("=" * 70)

children_count = 0
for child in soup.children:
    children_count += 1
    if children_count <= 5:
        print(f"  Child {children_count}: {repr(child)[:50]}")

print(f"\nTotal children: {children_count}")

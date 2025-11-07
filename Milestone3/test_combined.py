#!/usr/bin/env python3
"""
Test Cases 4, 5, 6: Combined tests for SoupReplacer

Test 4: Using multiple transformers together
Test 5: Backwards compatibility with M2 approach
Test 6: Edge cases


"""

import sys
import os

# Add the local beautifulsoup library to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup, SoupReplacer

def test4_combined_transformers():
    """Test using name_xformer and attrs_xformer together."""
    print("="*70)
    print("TEST 4: Multiple Transformers Combined")
    print("="*70)
    
    html = "<html><body><b class='old'>Bold</b><i>Italic</i></body></html>"
    print(f"Input: {html}")
    
    replacer = SoupReplacer(
        name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name,
        attrs_xformer=lambda tag: {"class": "new"} if tag.name in ["b", "strong"] else tag.attrs
    )
    
    soup = BeautifulSoup(html, 'html.parser', replacer=replacer)
    result = str(soup)
    
    print(f"Output: {result}")
    
    passed = "<strong" in result and 'class="new"' in result and "<b>" not in result
    print(f"\n{'✓ TEST 4 PASSED' if passed else '✗ TEST 4 FAILED'}")
    return passed

def test5_backwards_compatibility():
    """Test that M2 simple replacement still works."""
    print("\n" + "="*70)
    print("TEST 5: Backwards Compatibility with M2")
    print("="*70)
    
    html = "<html><body><b>Bold</b><i>Italic</i></body></html>"
    print(f"Input: {html}")
    
    # M2 style - simple string replacement
    replacer = SoupReplacer("b", "strong")
    soup = BeautifulSoup(html, 'html.parser', replacer=replacer)
    result = str(soup)
    
    print(f"Output: {result}")
    
    passed = "<strong>" in result and "<b>" not in result and "<i>" in result
    print(f"\n{'✓ TEST 5 PASSED' if passed else '✗ TEST 5 FAILED'}")
    return passed

def test6_edge_cases():
    """Test edge cases like nested tags and empty attributes."""
    print("\n" + "="*70)
    print("TEST 6: Edge Cases")
    print("="*70)
    
    # Edge case 1: Nested tags of same type
    html1 = "<div><b>Outer <b>Inner</b> text</b></div>"
    print(f"Test 6a - Nested tags: {html1}")
    
    replacer1 = SoupReplacer(name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name)
    soup1 = BeautifulSoup(html1, 'html.parser', replacer=replacer1)
    result1 = str(soup1)
    print(f"Result: {result1}")
    
    test_a = "<b>" not in result1 and result1.count("<strong>") == 2
    print(f"  {'✓' if test_a else '✗'} Nested tags handled")
    
    # Edge case 2: Tags with no attributes
    html2 = "<p>No attrs</p>"
    print(f"\nTest 6b - No attributes: {html2}")
    
    replacer2 = SoupReplacer(attrs_xformer=lambda tag: {**tag.attrs, "new": "attr"} if tag.name == "p" else tag.attrs)
    soup2 = BeautifulSoup(html2, 'html.parser', replacer=replacer2)
    result2 = str(soup2)
    print(f"Result: {result2}")
    
    test_b = 'new="attr"' in result2
    print(f"  {'✓' if test_b else '✗'} Attributes added to tag with no attrs")
    
    # Edge case 3: Transformer returns None (should not crash)
    html3 = "<div>Content</div>"
    print(f"\nTest 6c - Transformer returns None: {html3}")
    
    replacer3 = SoupReplacer(name_xformer=lambda tag: None)  # Returns None
    soup3 = BeautifulSoup(html3, 'html.parser', replacer=replacer3)
    result3 = str(soup3)
    print(f"Result: {result3}")
    
    test_c = "<div>" in result3  # Should keep original name
    print(f"  {'✓' if test_c else '✗'} Handles None return gracefully")
    
    all_passed = test_a and test_b and test_c
    print(f"\n{'✓ TEST 6 PASSED' if all_passed else '✗ TEST 6 FAILED'}")
    return all_passed

if __name__ == "__main__":
    results = [
        test4_combined_transformers(),
        test5_backwards_compatibility(),
        test6_edge_cases()
    ]
    
    print("\n" + "="*70)
    print(f"OVERALL: {sum(results)}/3 tests passed")
    print("="*70)
    
    sys.exit(0 if all(results) else 1)
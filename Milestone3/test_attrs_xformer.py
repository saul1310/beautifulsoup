
"""
Test Case 2: attrs_xformer - Transform tag attributes using a function

Tests the attrs_xformer parameter which allows modifying tag attributes.


"""

import sys
import os

# Add the local beautifulsoup library to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup, SoupReplacer

def test_attrs_xformer():
    """Test attrs_xformer to add class attributes."""
    
    print("="*70)
    print("TEST 2: attrs_xformer - Transform Tag Attributes")
    print("="*70)
    
    html = """
    <html>
        <body>
            <p>Paragraph 1</p>
            <p class="existing">Paragraph 2</p>
            <div>A div</div>
        </body>
    </html>
    """
    
    print("Input HTML:")
    print(html)
    
    # Transformer to add class="test" to all <p> tags
    def add_test_class(tag):
        """Add class='test' to all p tags."""
        if tag.name == "p":
            new_attrs = tag.attrs.copy()
            new_attrs["class"] = "test"
            return new_attrs
        return tag.attrs
    
    print("\nTransformation rule:")
    print("  Add class='test' to all <p> tags")
    
    replacer = SoupReplacer(attrs_xformer=add_test_class)
    print(f"\nCreated: {replacer}")
    
    soup = BeautifulSoup(html, 'html.parser', replacer=replacer)
    result = str(soup)
    
    print("\nOutput HTML:")
    print(soup.prettify())
    
    # Verify
    print("\nVerification:")
    p_tags = soup.find_all('p')
    all_have_test_class = all(tag.get('class') == ['test'] for tag in p_tags)
    div_unchanged = soup.find('div').attrs == {}
    
    checks = [
        (len(p_tags) == 2, f"✓ Found {len(p_tags)} <p> tags"),
        (all_have_test_class, "✓ All <p> tags have class='test'"),
        (div_unchanged, "✓ <div> attributes unchanged")
    ]
    
    all_passed = True
    for passed, message in checks:
        print(f"  {message if passed else '✗ ' + message[2:]}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n✓ TEST 2 PASSED: attrs_xformer works correctly!")
    else:
        print("\n✗ TEST 2 FAILED: Some checks did not pass")
    
    return all_passed

if __name__ == "__main__":
    success = test_attrs_xformer()
    sys.exit(0 if success else 1)
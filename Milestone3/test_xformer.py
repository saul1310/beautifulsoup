
"""
Test Case 3: xformer - Side-effect transformer

Tests the xformer parameter which modifies tags in place without returning values.


"""

import sys
import os

# Add the local beautifulsoup library to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup, SoupReplacer

def test_xformer():
    """Test xformer to remove class attributes."""
    
    print("="*70)
    print("TEST 3: xformer - Side-Effect Transformations")
    print("="*70)
    
    html = """
    <html>
        <body>
            <div class="container" id="main">Content</div>
            <p class="text" style="color:red">Paragraph</p>
            <span>No attributes</span>
        </body>
    </html>
    """
    
    print("Input HTML:")
    print(html)
    
    # Transformer that removes class attributes
    def remove_class_attr(tag):
        """Remove class attribute from all tags (side effect)."""
        if "class" in tag.attrs:
            del tag.attrs["class"]
    
    print("\nTransformation rule:")
    print("  Remove 'class' attribute from all tags")
    
    replacer = SoupReplacer(xformer=remove_class_attr)
    print(f"\nCreated: {replacer}")
    
    soup = BeautifulSoup(html, 'html.parser', replacer=replacer)
    result = str(soup)
    
    print("\nOutput HTML:")
    print(soup.prettify())
    
    # Verify
    print("\nVerification:")
    all_tags = soup.find_all()
    has_class = [tag for tag in all_tags if tag.get('class')]
    has_id = soup.find(id="main") is not None
    has_style = soup.find(attrs={"style": "color:red"}) is not None
    
    checks = [
        (len(has_class) == 0, f"✓ No tags have 'class' attribute (found {len(has_class)})"),
        (has_id, "✓ 'id' attribute preserved"),
        (has_style, "✓ 'style' attribute preserved")
    ]
    
    all_passed = True
    for passed, message in checks:
        print(f"  {message if passed else '✗ ' + message[2:]}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n✓ TEST 3 PASSED: xformer works correctly!")
    else:
        print("\n✗ TEST 3 FAILED: Some checks did not pass")
    
    return all_passed

if __name__ == "__main__":
    success = test_xformer()
    sys.exit(0 if success else 1)
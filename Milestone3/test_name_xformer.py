
"""
Test Case 1: name_xformer - Transform tag names using a function

Tests the name_xformer parameter which allows custom logic for tag name transformation.


"""

import sys
import os

# Add the local beautifulsoup library to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # Goes to beautifulsoup folder
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup, SoupReplacer

def test_name_xformer():
    """Test name_xformer with multiple tag replacements."""
    
    print("="*70)
    print("TEST 1: name_xformer - Transform Tag Names")
    print("="*70)
    
    # Test HTML with multiple tags to transform
    html = """
    <html>
        <body>
            <b>Bold text</b>
            <i>Italic text</i>
            <strike>Strikethrough</strike>
            <div>Normal div</div>
        </body>
    </html>
    """
    
    print("Input HTML:")
    print(html)
    
    # Define a transformer that modernizes old HTML tags
    def modernize_tags(tag):
        """Transform old HTML tags to modern equivalents."""
        replacements = {
            "b": "strong",
            "i": "em",
            "strike": "del"
        }
        return replacements.get(tag.name, tag.name)
    
    print("\nTransformation rules:")
    print("  b -> strong")
    print("  i -> em")
    print("  strike -> del")
    print("  (other tags unchanged)")
    
    # Create replacer with name_xformer
    replacer = SoupReplacer(name_xformer=modernize_tags)
    print(f"\nCreated: {replacer}")
    
    # Parse with the replacer
    soup = BeautifulSoup(html, 'html.parser', replacer=replacer)
    result = str(soup)
    
    print("\nOutput HTML:")
    print(soup.prettify())
    
    # Verify results
    print("\nVerification:")
    checks = [
        ("<b>" not in result, "✓ No <b> tags found"),
        ("<strong>" in result, "✓ <strong> tags found"),
        ("<i>" not in result, "✓ No <i> tags found"),
        ("<em>" in result, "✓ <em> tags found"),
        ("<strike>" not in result, "✓ No <strike> tags found"),
        ("<del>" in result, "✓ <del> tags found"),
        ("<div>" in result, "✓ <div> unchanged")
    ]
    
    all_passed = True
    for passed, message in checks:
        print(f"  {message if passed else '✗ ' + message[2:]}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n✓ TEST 1 PASSED: name_xformer works correctly!")
    else:
        print("\n✗ TEST 1 FAILED: Some checks did not pass")
    
    return all_passed

if __name__ == "__main__":
    success = test_name_xformer()
    sys.exit(0 if success else 1)
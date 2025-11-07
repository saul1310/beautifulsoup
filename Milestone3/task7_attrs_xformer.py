
"""
Task 7 (Milestone 3): Add class="test" to all <p> tags using attrs_xformer

This implements the same functionality as Milestone 1 Task 7, but uses
the new SoupReplacer attrs_xformer API to apply transformations during parsing.

Usage: python task7_attrs_xformer.py <input_file>


"""

import sys
import os

# Add the local beautifulsoup library to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4 import BeautifulSoup, SoupReplacer, XMLParsedAsHTMLWarning
import warnings

def add_test_class_to_p_tags(input_file):
    """
    Add class="test" to all <p> tags using SoupReplacer with attrs_xformer.
    Replacement happens during parsing for optimal performance.
    """
    try:
        # Read input file
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.lstrip()
        
        print(f"Processing '{input_file}'...")
        print("Adding class='test' to all <p> tags using attrs_xformer...\n")
        
        # Define attribute transformer function
        def add_test_class(tag):
            """
            Transformer that adds class='test' to all <p> tags.
            
            For <p> tags: Add or replace class attribute with 'test'
            For other tags: Keep attributes unchanged
            """
            if tag.name == "p":
                # Create new attributes dict with class="test"
                new_attrs = tag.attrs.copy()
                new_attrs["class"] = "test"
                return new_attrs
            # Return unchanged attributes for non-<p> tags
            return tag.attrs
        
        # Create SoupReplacer with attrs_xformer
        replacer = SoupReplacer(attrs_xformer=add_test_class)
        print(f"Created: {replacer}\n")
        
        # Parse with replacer - transformation happens during parsing!
        try:
            soup = BeautifulSoup(content, 'xml', replacer=replacer)
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            soup = BeautifulSoup(content, 'html.parser', replacer=replacer)
        
        # Count modified tags
        p_tags = soup.find_all('p')
        p_with_test_class = [tag for tag in p_tags if tag.get('class') == ['test']]
        
        print(f"Results:")
        print(f"  Total <p> tags found: {len(p_tags)}")
        print(f"  <p> tags with class='test': {len(p_with_test_class)}")
        
        # Determine output filename
        base_name = os.path.splitext(input_file)[0]
        ext = '.xml' if input_file.lower().endswith('.xml') else '.html'
        output_file = f"{base_name}_p_class_test{ext}"
        
        # Write output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print(f"\nSuccess! Output written to: {output_file}")
        print(f"All {len(p_tags)} <p> tags now have class='test'")
        
        # Show sample of modifications
        if p_tags:
            print("\nSample of modified <p> tags:")
            for i, tag in enumerate(p_tags[:3], 1):
                print(f"  {i}. {tag}")
            if len(p_tags) > 3:
                print(f"  ... and {len(p_tags) - 3} more")
        
        # Verification
        print("\nVerification (re-parsing output):")
        with open(output_file, 'r', encoding='utf-8-sig') as f:
            verify_content = f.read().lstrip()
        
        try:
            verify_soup = BeautifulSoup(verify_content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            verify_soup = BeautifulSoup(verify_content, 'html.parser')
        
        verify_p_tags = verify_soup.find_all('p')
        verify_with_test = [tag for tag in verify_p_tags if tag.get('class') == ['test']]
        
        print(f"  <p> tags in output: {len(verify_p_tags)}")
        print(f"  With class='test': {len(verify_with_test)}")
        
        if len(verify_with_test) == len(verify_p_tags):
            print("  ✓ All <p> tags have class='test'")
        else:
            print("  ⚠ Warning: Not all <p> tags have class='test'")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task7_attrs_xformer.py <input_file>")
        print("\nThis program uses SoupReplacer with attrs_xformer to add")
        print("class='test' to all <p> tags during parsing (Milestone 3 approach).")
        print("\nComparison:")
        print("  Milestone 1: Parse → Find all <p> → Modify each → Write (2 passes)")
        print("  Milestone 3: Parse with transformation (1 pass)")
        sys.exit(1)
    
    input_file = sys.argv[1]
    add_test_class_to_p_tags(input_file)
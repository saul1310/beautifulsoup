## How to Run Tests

### Prerequisites
- Python 3.7 or higher
- Modified BeautifulSoup source code in `beautifulsoup/bs4/`

### Running Individual Tests
```bash
cd beautifulsoup/Milestone3

# Test 1: name_xformer
python test_name_xformer.py

# Test 2: attrs_xformer
python test_attrs_xformer.py

# Test 3: xformer (side effects)
python test_xformer.py

# Tests 4, 5, 6: Combined tests
python test_combined.py
```

### Running Task 7
```bash
# Task 7: Add class="test" to all <p> tags
python task7_attrs_xformer.py test.html

# Output will be written to: test_p_class_test.html
```

### Expected Results

All tests should output `✓ TEST X PASSED` messages.

Task 7 should report:
- Total `<p>` tags found
- All `<p>` tags modified with `class='test'`
- Output file created successfully

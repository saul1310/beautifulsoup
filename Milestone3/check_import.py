import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
beautifulsoup_path = os.path.join(parent_dir, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_path)

from bs4.filter import SoupReplacer
import inspect

print("SoupReplacer location:", inspect.getfile(SoupReplacer))
print("\nSoupReplacer.__init__ signature:")
print(inspect.signature(SoupReplacer.__init__))
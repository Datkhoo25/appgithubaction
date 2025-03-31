import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from math_operation import add, sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_subtract():
    assert sub(2,3)==-1
    assert add(7,5)==2
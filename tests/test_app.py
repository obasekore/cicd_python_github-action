import sys
sys.path.append('network')
from app import index

def test_index():
    assert index() == "Hello, world!"


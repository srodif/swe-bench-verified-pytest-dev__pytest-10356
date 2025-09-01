"""
Standalone test to verify the multiple inheritance test case works as expected
"""
import pytest
from _pytest.pytester import Pytester
from _pytest.config import Config

# Minimal test setup 
def test_multiple_inheritance():
    """Test the multiple inheritance test case in isolation."""
    
    # Create the test content
    test_content = """
import pytest

@pytest.mark.foo
class Foo(object):
    pass

@pytest.mark.bar
class Bar(object):
    pass

class TestMultiple(Foo, Bar):
    def test_dings(self):
        pass

class TestTriple(Foo, Bar):
    @pytest.mark.baz
    def test_more(self):
        pass
"""
    
    # Write to a temp file and test
    with open('/tmp/test_multiple.py', 'w') as f:
        f.write(test_content)
    
    # Import and analyze the classes directly
    import sys
    sys.path.insert(0, '/tmp')
    
    try:
        import test_multiple
        
        from _pytest.mark.structures import get_unpacked_marks
        
        # Test that classes have expected marks
        multiple_marks = [m.name for m in get_unpacked_marks(test_multiple.TestMultiple)]
        print("TestMultiple marks:", multiple_marks)
        assert set(multiple_marks) == {"foo", "bar"}
        
        triple_marks = [m.name for m in get_unpacked_marks(test_multiple.TestTriple)]  
        print("TestTriple marks:", triple_marks)
        assert set(triple_marks) == {"foo", "bar"}
        
        print("Multiple inheritance test passed!")
        
    finally:
        if 'test_multiple' in sys.modules:
            del sys.modules['test_multiple']

if __name__ == "__main__":
    test_multiple_inheritance()
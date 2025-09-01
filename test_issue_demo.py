"""
Test to demonstrate the MRO marker collection issue
"""
import pytest
from _pytest.python import Class
from _pytest.mark.structures import get_unpacked_marks


@pytest.mark.foo
class Foo:
    pass


@pytest.mark.bar  
class Bar:
    pass


class TestDings(Foo, Bar):
    def test_dings(self):
        pass


def test_marker_collection():
    """Test that demonstrates the issue with marker collection"""
    
    # Create a Class collector for TestDings
    class FakeParent:
        obj = None
        
    # Simulate what happens during test collection
    print("Direct marks on classes:")
    print(f"Foo marks: {[m.name for m in get_unpacked_marks(Foo)]}")
    print(f"Bar marks: {[m.name for m in get_unpacked_marks(Bar)]}")
    print(f"TestDings marks: {[m.name for m in get_unpacked_marks(TestDings)]}")
    
    # Check MRO
    print(f"TestDings MRO: {[cls.__name__ for cls in TestDings.__mro__]}")
    
    # Check what pytestmark attributes exist
    print(f"Foo.pytestmark: {getattr(Foo, 'pytestmark', None)}")
    print(f"Bar.pytestmark: {getattr(Bar, 'pytestmark', None)}")
    print(f"TestDings.pytestmark: {getattr(TestDings, 'pytestmark', None)}")
    
    # The issue is that Python's normal attribute lookup via MRO 
    # means TestDings.pytestmark resolves to Foo.pytestmark (first in MRO)
    # So Bar's markers are never seen!
    
    # So only when we have pytestmark on TestDings itself do we get markers
    # But with MRO inheritance, we should get markers from all classes in the MRO


if __name__ == "__main__":
    test_marker_collection()
"""
Test for multiple inheritance marker collection (MRO)
"""
import pytest
from _pytest.mark.structures import get_unpacked_marks


def test_multiple_inheritance_marker_collection():
    """Test that marks from multiple base classes are collected."""
    
    @pytest.mark.foo
    class Foo:
        pass

    @pytest.mark.bar  
    class Bar:
        pass
        
    @pytest.mark.baz
    class Baz:
        pass

    class TestMultiple(Foo, Bar):
        def test_something(self):
            pass
            
    class TestTriple(Foo, Bar, Baz):
        def test_something(self):
            pass

    # Test that both markers are collected
    foo_marks = [m.name for m in get_unpacked_marks(Foo)]
    bar_marks = [m.name for m in get_unpacked_marks(Bar)]
    baz_marks = [m.name for m in get_unpacked_marks(Baz)]
    multiple_marks = [m.name for m in get_unpacked_marks(TestMultiple)]
    triple_marks = [m.name for m in get_unpacked_marks(TestTriple)]

    assert foo_marks == ['foo']
    assert bar_marks == ['bar'] 
    assert baz_marks == ['baz']
    assert set(multiple_marks) == {'foo', 'bar'}  # Both markers present
    assert set(triple_marks) == {'foo', 'bar', 'baz'}  # All three markers present
    
    # Test that MRO order is preserved (foo should come first in both cases)
    assert multiple_marks == ['foo', 'bar']
    assert triple_marks == ['foo', 'bar', 'baz']


def test_single_inheritance_still_works():
    """Test that single inheritance still works as before."""
    
    @pytest.mark.base
    class Base:
        pass
        
    @pytest.mark.derived  
    class Derived(Base):
        pass
        
    derived_marks = [m.name for m in get_unpacked_marks(Derived)]
    assert set(derived_marks) == {'base', 'derived'}
    # MRO order: derived first, then base (deduped so base only appears once)
    assert derived_marks == ['base', 'derived']


def test_no_inheritance_still_works():
    """Test that classes without inheritance still work."""
    
    @pytest.mark.single
    class Single:
        pass
        
    single_marks = [m.name for m in get_unpacked_marks(Single)]
    assert single_marks == ['single']


def test_non_class_objects_unchanged():
    """Test that non-class objects work as before."""
    
    @pytest.mark.func_mark
    def test_function():
        pass
        
    func_marks = [m.name for m in get_unpacked_marks(test_function)]
    assert func_marks == ['func_mark']


def test_diamond_inheritance():
    """Test diamond inheritance pattern."""
    
    @pytest.mark.base
    class Base:
        pass
        
    @pytest.mark.left
    class Left(Base):
        pass
        
    @pytest.mark.right  
    class Right(Base):
        pass
        
    class Diamond(Left, Right):
        def test_something(self):
            pass
            
    diamond_marks = [m.name for m in get_unpacked_marks(Diamond)]
    # Base marker should only appear once even though it's in MRO multiple times
    assert set(diamond_marks) == {'left', 'right', 'base'}
    # MRO order: Diamond, Left, Right, Base
    # Left.pytestmark = ['base', 'left'], Right.pytestmark = ['base', 'right'], Base.pytestmark = ['base']  
    # Deduplication keeps first occurrence: ['base', 'left', 'right']
    assert diamond_marks == ['base', 'left', 'right']


if __name__ == "__main__":
    test_multiple_inheritance_marker_collection()
    test_single_inheritance_still_works() 
    test_no_inheritance_still_works()
    test_non_class_objects_unchanged()
    test_diamond_inheritance()
    print("All tests passed!")
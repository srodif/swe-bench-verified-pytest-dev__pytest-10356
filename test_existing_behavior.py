"""
Test to verify that existing single inheritance behavior still works
"""
import pytest
from _pytest.mark.structures import get_unpacked_marks

# This simulates the existing test case
@pytest.mark.a
class Base(object):
    pass

@pytest.mark.b
class Test1(Base):
    def test_foo(self):
        pass

class Test2(Base):
    def test_bar(self):
        pass

def test_existing_single_inheritance():
    # Test1 should have both 'a' and 'b' marks
    test1_marks = [m.name for m in get_unpacked_marks(Test1)]
    assert set(test1_marks) == {'a', 'b'}
    print("Test1 marks:", test1_marks)
    
    # Test2 should only have 'a' mark
    test2_marks = [m.name for m in get_unpacked_marks(Test2)]  
    assert set(test2_marks) == {'a'}
    print("Test2 marks:", test2_marks)
    
    print("Single inheritance test passed!")

def test_multi_level_inheritance():
    # This simulates the multi-level inheritance test case
    
    @pytest.mark.a
    class Base(object): 
        pass

    @pytest.mark.b
    class Base2(Base): 
        pass

    @pytest.mark.c
    class Test1(Base2):
        def test_foo(self): 
            pass

    class Test2(Base2):
        def test_bar(self): 
            pass
    
    test1_marks = [m.name for m in get_unpacked_marks(Test1)]
    test2_marks = [m.name for m in get_unpacked_marks(Test2)]
    
    assert set(test1_marks) == {'a', 'b', 'c'}
    assert set(test2_marks) == {'a', 'b'}
    
    print("Test1 marks:", test1_marks)
    print("Test2 marks:", test2_marks)
    print("Multi-level inheritance test passed!")

if __name__ == "__main__":
    test_existing_single_inheritance()
    test_multi_level_inheritance()
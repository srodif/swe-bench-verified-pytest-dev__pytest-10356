import pytest
from _pytest.mark.structures import get_unpacked_marks

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

print("Diamond MRO:", [cls.__name__ for cls in Diamond.__mro__])

# Check what's in each class's __dict__
for cls in Diamond.__mro__:
    print(f"{cls.__name__}.__dict__ has pytestmark: {'pytestmark' in cls.__dict__}")
    if 'pytestmark' in cls.__dict__:
        marks = cls.__dict__['pytestmark']
        if isinstance(marks, list):
            print(f"  {cls.__name__} pytestmark: {[m.name for m in marks]}")
        else:
            print(f"  {cls.__name__} pytestmark: {marks.name}")

diamond_marks = [m.name for m in get_unpacked_marks(Diamond)]
print("Diamond marks:", diamond_marks)
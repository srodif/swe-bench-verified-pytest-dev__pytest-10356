import pytest
from _pytest.mark.structures import get_unpacked_marks

@pytest.mark.base
class Base:
    pass
    
@pytest.mark.derived  
class Derived(Base):
    pass

print("Derived MRO:", [cls.__name__ for cls in Derived.__mro__])

# Let's check what's in each class's __dict__
for cls in Derived.__mro__:
    print(f"{cls.__name__}.__dict__ has pytestmark: {'pytestmark' in cls.__dict__}")
    if 'pytestmark' in cls.__dict__:
        marks = cls.__dict__['pytestmark']
        if isinstance(marks, list):
            print(f"  {cls.__name__} pytestmark: {[m.name for m in marks]}")
        else:
            print(f"  {cls.__name__} pytestmark: {marks.name}")
            
print()

# Now let's see what our function returns
derived_marks = list(get_unpacked_marks(Derived))
print("get_unpacked_marks result:")
for mark in derived_marks:
    print(f"  {mark.name}")
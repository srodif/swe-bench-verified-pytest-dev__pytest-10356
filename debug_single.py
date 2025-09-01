import pytest
from _pytest.mark.structures import get_unpacked_marks

@pytest.mark.base
class Base:
    pass
    
@pytest.mark.derived  
class Derived(Base):
    pass
    
print("Derived MRO:", [cls.__name__ for cls in Derived.__mro__])
derived_marks = [m.name for m in get_unpacked_marks(Derived)]
print("Derived marks:", derived_marks)
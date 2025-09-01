import pytest


@pytest.mark.foo
class Foo:
    pass


@pytest.mark.bar
class Bar:
    pass


class TestDings(Foo, Bar):
    def test_dings(self):
        # This test should have both markers, foo and bar.
        # In practice markers are resolved using MRO (so foo wins)
        pass


if __name__ == "__main__":
    # Test script to check marks
    from _pytest.mark.structures import get_unpacked_marks
    
    print("Marks on TestDings:")
    marks = list(get_unpacked_marks(TestDings))
    for mark in marks:
        print(f"  - {mark.name}")
    
    print("\nMarks on Foo:")
    marks = list(get_unpacked_marks(Foo))
    for mark in marks:
        print(f"  - {mark.name}")
        
    print("\nMarks on Bar:")
    marks = list(get_unpacked_marks(Bar))
    for mark in marks:
        print(f"  - {mark.name}")
        
    print("\nMRO of TestDings:", TestDings.__mro__)
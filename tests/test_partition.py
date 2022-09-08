from main import partition

def test_partition() -> None:
    pivot = partition([6,4,2,5,3,1], 2, 4)
    assert pivot == 3
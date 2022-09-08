from main import InsertionSort

def test_bubble_sort() -> None:
    sorted_array = InsertionSort([6, 4, 2, 5, 3, 1])
    assert sorted_array == [1, 2, 3, 4, 5, 6]
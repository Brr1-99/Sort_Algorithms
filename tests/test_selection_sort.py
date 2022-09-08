from main import SelectionSort

def test_bubble_sort() -> None:
    sorted_array = SelectionSort([6, 4, 2, 5, 3, 1])
    assert sorted_array == [1, 2, 3, 4, 5, 6]